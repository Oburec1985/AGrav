import logging
import sys
from typing import List, Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

from src.database import MemoryDatabase

# Настройка логирования в stderr (чтобы не нарушать JSON-RPC протокол в stdout)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    stream=sys.stderr
)
logger = logging.getLogger("mcp_memory_db")

# Создаем экземпляр MCP-сервера
mcp = FastMCP("MemoryDB")

# Инициализируем локальную базу данных
try:
    db = MemoryDatabase()
    logger.info("Local Qdrant database initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize database: {e}")
    sys.exit(1)

@mcp.tool()
def save_memory_fact(
    fact: str, 
    tags: List[str], 
    project_context: Optional[str] = None, 
    source_file: Optional[str] = None
) -> str:
    """
    Сохранить важный факт, решение или правило разработки в долговременную семантическую память.
    
    :param fact: Текст факта или решения (например, "Lazarus LCL captions в cp1251 требуют кодирования в UTF-8").
    :param tags: Список меток для фильтрации (например, ["delphi", "encoding", "lazarus"]).
    :param project_context: Имя проекта, к которому относится факт (например, "RecorderLnx", "ALF", "SQLSensorsDB").
    :param source_file: Относительный путь к файлу-источнику (например, "20_Проекты/OglChart/architecture.md").
    :return: Идентификатор сохраненной записи (UUID).
    """
    try:
        fact_id = db.save_fact(fact, tags, project_context, source_file)
        logger.info(f"Saved fact {fact_id} successfully.")
        return f"Факт сохранен с ID: {fact_id}"
    except Exception as e:
        logger.error(f"Error saving fact: {e}")
        return f"Ошибка при сохранении факта: {str(e)}"

@mcp.tool()
def search_memory_facts(
    query: str, 
    limit: int = 5, 
    tags: Optional[List[str]] = None, 
    project_context: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Семантический (смысловой) поиск по сохраненным фактам памяти.
    
    Выполняет косинусный поиск сходства векторов и возвращает наиболее релевантные результаты.
    
    :param query: Запрос на естественном языке (например, "проблема с кодировкой кириллицы").
    :param limit: Максимальное количество возвращаемых результатов (по умолчанию 5).
    :param tags: Фильтр по тегам (например, ["encoding"]). Будут возвращены только факты, содержащие эти теги.
    :param project_context: Фильтр по контексту проекта (например, "RecorderLnx").
    :return: Список найденных фактов с оценкой релевантности (score).
    """
    try:
        logger.info(f"Searching facts for query: '{query}'")
        results = db.search_facts(query, limit, tags, project_context)
        return results
    except Exception as e:
        logger.error(f"Error searching facts: {e}")
        return [{"error": f"Ошибка при поиске: {str(e)}"}]

@mcp.tool()
def delete_memory_fact(fact_id: str) -> str:
    """
    Удалить факт из памяти по его идентификатору UUID.
    
    :param fact_id: Строковый идентификатор UUID удаляемой записи.
    :return: Статус удаления.
    """
    try:
        success = db.delete_fact(fact_id)
        if success:
            logger.info(f"Deleted fact {fact_id} successfully.")
            return f"Факт {fact_id} успешно удален."
        else:
            return f"Факт {fact_id} не найден или не может быть удален."
    except Exception as e:
        logger.error(f"Error deleting fact {fact_id}: {e}")
        return f"Ошибка при удалении факта: {str(e)}"

@mcp.tool()
def list_memory_facts(limit: int = 50) -> List[Dict[str, Any]]:
    """
    Вывести список последних сохраненных фактов, упорядоченных по времени создания (новые сверху).
    
    :param limit: Количество выводимых фактов (по умолчанию 50).
    :return: Список фактов с метаданными.
    """
    try:
        return db.list_facts(limit)
    except Exception as e:
        logger.error(f"Error listing facts: {e}")
        return [{"error": f"Ошибка при выводе списка: {str(e)}"}]

if __name__ == "__main__":
    # Запускаем MCP сервер с использованием stdio транспорта (обмен по stdin/stdout)
    mcp.run(transport='stdio')
