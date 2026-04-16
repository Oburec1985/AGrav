from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel, create_engine, Session, select
from .logger import trace, logger

# --- Модели Базы Данных ---

class Manufacturer(SQLModel, table=True):
    """Таблица производителей оборудования."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    country: Optional[str] = None

class Category(SQLModel, table=True):
    """Иерархическая таблица категорий (типов измерений)."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")
    suggested_specs: List["CategorySpecMapping"] = Relationship(back_populates="category")

class CategorySpecMapping(SQLModel, table=True):
    """Справочник разрешенных/рекомендуемых параметров для каждой категории."""
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="category.id")
    param_name: str # Имя из ProductSpec (напр. "sensitivity")
    
    category: Category = Relationship(back_populates="suggested_specs")

class Product(SQLModel, table=True):
    """Основной реестр датчиков и аксессуаров."""
    id: Optional[int] = Field(default=None, primary_key=True)
    model: str = Field(index=True)
    full_name: str
    description: Optional[str] = None
    price: Optional[float] = None
    is_gosreestr: bool = Field(default=False)
    url: Optional[str] = None
    image_url: Optional[str] = None
    
    manufacturer_id: int = Field(foreign_key="manufacturer.id")
    category_id: int = Field(foreign_key="category.id")
    
    # Связи
    manufacturer: Manufacturer = Relationship(sa_relationship_kwargs={"lazy": "joined"})
    category: Category = Relationship()
    specs: List["ProductSpec"] = Relationship(
        back_populates="product", 
        cascade_delete=True,
        sa_relationship_kwargs={"lazy": "selectin"} # Рекомендуется для коллекций
    )

class ProductSpec(SQLModel, table=True):
    """
    Характеристики датчиков (EAV модель) с поддержкой номиналов и условий.
    
    Данная структура позволяет гибко хранить бесконечное количество параметров
    без изменения схемы базы данных. Номинал и условия используются для 
    интеллектуального подбора логгера в интерфейсе.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    
    group_name: str = Field(index=True) # Метрология, Конструктив, Сигнал и т.д.
    param_name: str = Field(index=True)
    param_value: str # Текстовое описание (напр. "±2% в диапазоне")
    
    # Числовые поля для математических расчетов и фильтрации
    nominal_value: Optional[float] = None
    numeric_value_min: Optional[float] = None
    numeric_value_max: Optional[float] = None
    unit: Optional[str] = None # Единица измерения (В, Гц, Па)
    
    # Квалификатор (напр. "±5%", "With steel tip"). 
    # Критично для параметров АЧХ, зависящих от погрешности.
    condition: Optional[str] = None 

    # Обратная связь с продуктом
    product: "Product" = Relationship()

# --- Утилиты ---

@trace
def init_db(engine):
    """
    Инициализация таблиц в базе данных.
    
    Функция создает физические таблицы в SQLite файле на основе
    всех классов, унаследованных от SQLModel.
    """
    logger.info("Initializing database tables...")
    SQLModel.metadata.create_all(engine)
    logger.info("Database initialized successfully.")
