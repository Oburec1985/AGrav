import os
from pathlib import Path

# Базовый каталог проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Каталог для данных (БД)
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Каталог для хранения отдельных текстовых файлов фактов (для отслеживания в Git)
RECORDS_DIR = DATA_DIR / "records"
RECORDS_DIR.mkdir(parents=True, exist_ok=True)

# Путь к локальному файлу базы данных Qdrant (через SQLite под капотом)
DB_PATH = os.getenv("MEMORY_DB_PATH", str(DATA_DIR / "memory_store.db"))

# Настройки эмбеддингов
# Модель sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 поддерживает русский и английский
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Имя коллекции в Qdrant
COLLECTION_NAME = "agent_memories"
NOTES_COLLECTION_NAME = "vault_notes"
SOURCE_COLLECTION_NAME = "source_code"

# Read-only source trees indexed for semantic code archaeology.
ORIGINAL_RECORDER_ROOT = Path(os.getenv(
    "ORIGINAL_RECORDER_ROOT", r"D:\works\windev-v3.9"
))
ORIGINAL_RECORDER_DIRS = tuple(filter(None, os.getenv(
    "ORIGINAL_RECORDER_DIRS",
    "mr;rc_core;rc_guisrv;rc_conui;rc_ctrpn;rc_utils;plugins/rcsdk;"
    "mtc;mtcEthernet81;mdpEthernet81;MIC140_96_rce;MIC140pp_rce;devapi;"
    "examples/mebius.daq"
).split(";")))

# Путь к локальному кэшу модели ONNX (чтобы не скачивать из сети при каждом развертывании)
MODEL_CACHE_DIR = os.getenv("MODEL_CACHE_DIR", str(BASE_DIR / "model_cache"))
