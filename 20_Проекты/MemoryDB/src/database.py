import json
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue, MatchAny

from src.config import DB_PATH, COLLECTION_NAME, RECORDS_DIR
from src.embeddings import LocalEmbedder

class MemoryDatabase:
    """Интерфейс к локальному хранилищу Qdrant Client в режиме offline-файла."""
    
    def __init__(self):
        self.client = QdrantClient(path=DB_PATH)
        self.embedder = LocalEmbedder()
        self._ensure_collection()
        self._sync_with_disk()
        
    def _sync_with_disk(self):
        """
        Синхронизирует локальную базу данных Qdrant с текстовыми JSON-файлами в RECORDS_DIR.
        Файлы на диске являются первоисточником.
        """
        import glob
        from pathlib import Path
        
        # 1. Читаем все JSON файлы из RECORDS_DIR
        local_records = {}
        json_files = glob.glob(str(RECORDS_DIR / "*.json"))
        for file_path in json_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "id" in data and "fact" in data:
                        local_records[data["id"]] = data
            except Exception as e:
                import sys
                print(f"Ошибка чтения файла {file_path}: {e}", file=sys.stderr)
                
        # 2. Получаем все существующие точки из Qdrant
        qdrant_records = {}
        try:
            points, _ = self.client.scroll(
                collection_name=COLLECTION_NAME,
                limit=10000,
                with_payload=True,
                with_vectors=False
            )
            for pt in points:
                qdrant_records[pt.id] = pt.payload
        except Exception as e:
            import sys
            print(f"Ошибка при получении данных из Qdrant: {e}", file=sys.stderr)

        # 3. Синхронизируем: удаляем то, чего нет на диске
        ids_to_delete = []
        for qid in qdrant_records:
            if qid not in local_records:
                ids_to_delete.append(qid)
                
        if ids_to_delete:
            try:
                self.client.delete(
                    collection_name=COLLECTION_NAME,
                    points_selector=ids_to_delete
                )
                print(f"Удалено устаревших записей из Qdrant: {len(ids_to_delete)}")
            except Exception as e:
                import sys
                print(f"Ошибка при удалении записей из Qdrant: {e}", file=sys.stderr)

        # 4. Синхронизируем: добавляем или обновляем то, что изменилось/появилось
        points_to_upsert = []
        for lid, lrec in local_records.items():
            need_upsert = False
            if lid not in qdrant_records:
                need_upsert = True
            else:
                qrec = qdrant_records[lid]
                if (lrec.get("fact") != qrec.get("fact") or 
                    lrec.get("tags") != qrec.get("tags") or 
                    lrec.get("project_context") != qrec.get("project_context") or
                    lrec.get("source_file") != qrec.get("source_file")):
                    need_upsert = True
                    
            if need_upsert:
                try:
                    vector = self.embedder.get_embedding(lrec["fact"])
                    payload = {
                        "id": lid,
                        "fact": lrec["fact"],
                        "tags": lrec.get("tags", []),
                        "project_context": lrec.get("project_context", "global"),
                        "source_file": lrec.get("source_file"),
                        "created_at": lrec.get("created_at", datetime.utcnow().isoformat())
                    }
                    points_to_upsert.append(
                        PointStruct(
                            id=lid,
                            vector=vector,
                            payload=payload
                        )
                    )
                except Exception as e:
                    import sys
                    print(f"Ошибка подготовки вектора для ID {lid}: {e}", file=sys.stderr)

        if points_to_upsert:
            try:
                self.client.upsert(
                    collection_name=COLLECTION_NAME,
                    points=points_to_upsert
                )
                print(f"Синхронизировано/обновлено записей в Qdrant: {len(points_to_upsert)}")
            except Exception as e:
                import sys
                print(f"Ошибка пакетной вставки в Qdrant: {e}", file=sys.stderr)

        
    def _ensure_collection(self):
        """Проверяет существование коллекции и создает ее при необходимости."""
        if not self.client.collection_exists(COLLECTION_NAME):
            vector_size = self.embedder.get_vector_size()
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
            )
            
    def save_fact(
        self, 
        fact: str, 
        tags: List[str], 
        project_context: Optional[str] = None, 
        source_file: Optional[str] = None
    ) -> str:
        """
        Сохраняет факт в базу данных, генерируя эмбеддинг и присваивая UUID.
        
        Возвращает строковый ID сохраненной записи.
        """
        fact_id = str(uuid.uuid4())
        vector = self.embedder.get_embedding(fact)
        
        payload = {
            "id": fact_id,
            "fact": fact,
            "tags": tags,
            "project_context": project_context or "global",
            "source_file": source_file,
            "created_at": datetime.utcnow().isoformat()
        }
        
        # Запись на диск
        file_path = RECORDS_DIR / f"{fact_id}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
            
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=fact_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )
        return fact_id
        
    def search_facts(
        self, 
        query: str, 
        limit: int = 5, 
        tags: Optional[List[str]] = None, 
        project_context: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Выполняет семантический поиск похожих фактов.
        
        Поддерживает фильтрацию по тегам и проектному контексту.
        """
        vector = self.embedder.get_embedding(query)
        
        # Построение фильтра
        must_conditions = []
        
        if project_context:
            must_conditions.append(
                FieldCondition(key="project_context", match=MatchValue(value=project_context))
            )
            
        if tags:
            must_conditions.append(
                FieldCondition(key="tags", match=MatchAny(any=tags))
            )
            
        query_filter = Filter(must=must_conditions) if must_conditions else None
        
        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector,
            query_filter=query_filter,
            limit=limit,
            with_payload=True
        ).points
        
        output = []
        for res in results:
            output.append({
                "id": res.id,
                "score": float(res.score),
                "fact": res.payload.get("fact"),
                "tags": res.payload.get("tags", []),
                "project_context": res.payload.get("project_context"),
                "created_at": res.payload.get("created_at")
            })
        return output
        
    def delete_fact(self, fact_id: str) -> bool:
        """Удаляет факт из базы данных по его ID."""
        file_path = RECORDS_DIR / f"{fact_id}.json"
        file_deleted = False
        try:
            if file_path.exists():
                file_path.unlink()
                file_deleted = True
        except Exception as e:
            import sys
            print(f"Ошибка при удалении файла {file_path}: {e}", file=sys.stderr)

        try:
            self.client.delete(
                collection_name=COLLECTION_NAME,
                points_selector=[fact_id]
            )
            return True
        except Exception:
            return file_deleted
            
    def list_facts(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Возвращает список последних сохраненных фактов."""
        records, _ = self.client.scroll(
            collection_name=COLLECTION_NAME,
            limit=limit,
            with_payload=True,
            with_vectors=False
        )
        
        output = []
        for rec in records:
            output.append({
                "id": rec.id,
                "fact": rec.payload.get("fact"),
                "tags": rec.payload.get("tags", []),
                "project_context": rec.payload.get("project_context"),
                "created_at": rec.payload.get("created_at")
            })
            
        # Сортировка по дате создания (новые сверху)
        output.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return output
