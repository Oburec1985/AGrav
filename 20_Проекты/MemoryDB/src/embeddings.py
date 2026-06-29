from typing import List
from fastembed import TextEmbedding
from src.config import EMBEDDING_MODEL_NAME, MODEL_CACHE_DIR

class LocalEmbedder:
    """Локальный генератор эмбеддингов с использованием ONNX моделей через FastEmbed."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LocalEmbedder, cls).__new__(cls)
            cls._instance._model = None
        return cls._instance
        
    @property
    def model(self) -> TextEmbedding:
        """Отложенная инициализация модели при первом запросе."""
        if self._model is None:
            # Инициализируем модель fastembed, используя локальный путь к ONNX файлам
            self._model = TextEmbedding(
                model_name=EMBEDDING_MODEL_NAME,
                specific_model_path=MODEL_CACHE_DIR
            )
        return self._model
        
    def get_embedding(self, text: str) -> List[float]:
        """Генерирует вектор эмбеддинга для одного текста."""
        # FastEmbed ориентирован на батчи документов
        embeddings = list(self.model.embed([text]))
        return [float(x) for x in embeddings[0]]
        
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Генерирует векторы эмбеддингов для списка текстов."""
        embeddings = list(self.model.embed(texts))
        return [[float(x) for x in emb] for emb in embeddings]
        
    def get_vector_size(self) -> int:
        """Возвращает размерность вектора модели."""
        # Для paraphrase-multilingual-MiniLM-L12-v2 размерность равна 384.
        # Вызовем пробный эмбеддинг для получения точной размерности
        sample = self.get_embedding("test")
        return len(sample)
