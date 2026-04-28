# Граф Знаний и Связей (Relationships)

Данный файл служит "картой памяти" репозитория AGrav, отслеживая зависимости между проектами, устройствами и методологиями.

## Легенда
- **Depends On** (-->): Компонент требует наличия другого для работы.
- **Implements** (--|>): Реализация абстрактной методики.
- **References** (-.-): Информационная связь.

## Карта Проектов и Систем

```mermaid
graph TD
    subgraph "00_Система"
        MainIndex["Оглавление.md"]
        Skills["Скиллы_ИИ.md"]
        RelMap["Relationships.md"]
        CodeStd["Код_Стандарты.md"]
        LocTool["Локализация_dxgettext.md"]
    end

    subgraph "15_Дом / Сети"
        Infrastructure["20_Инфраструктура_и_Серверы"]
        Devices["30_Устройства_и_Клиенты"]
        NodeTemp["Шаблон_Настройки_Узла.md"]
        Hiplet["Hiplet_138.124.85.38.md"]
        BypassWiki["40_Энциклопедия_Обхода"]
    end

    subgraph "20_Проекты"
        SQLSensors["SQLSensorsDB"]
        Bridge["Future API Bridge"]
        OglChart["OpenGLChartLazarus"]
        LegacyCChart["Delphi cChart"]
        LazarusFPC["Lazarus/FPC"]
    end

    %% Связи
    RelMap -.-> MainIndex
    Skills -.-> RelMap
    Skills --> CodeStd
    
    Infrastructure --> NodeTemp
    NodeTemp -.-> Hiplet
    
    SQLSensors -.-> Bridge
    Bridge -.-> Infrastructure
    OglChart -.-> LegacyCChart
    OglChart --> LazarusFPC
    OglChart --> CodeStd
    
    BypassWiki -.-> Devices
    BypassWiki -.-> Infrastructure
```

## Реестр Зависимостей (Log)

| Откуда | Куда | Тип связи | Описание |
| :--- | :--- | :--- | :--- |
| `Скиллы_ИИ.md` | `Код_Стандарты.md` | Depends On | Основные технические правила вынесены в стандарт. |
| `20_Инфраструктура_и_Серверы` | `Шаблон_Настройки_Узла.md` | Implements | Вся инфраструктура теперь строится по единому шаблону. |
| `SQLSensorsDB` | `15_Дом/Инфраструктура` | Potential Bridge | Планируемая связь для передачи данных с домашних датчиков в БД. |
| `OpenGLChartLazarus` | `Delphi cChart` | References | Новый Lazarus/FPC-компонент проектируется по мотивам существующего Delphi-компонента из `sharedUtils/компоненты/chart_dpk/chart`. |
| `OpenGLChartLazarus` | `Lazarus/FPC` | Depends On | Целевая среда разработки и компиляции кроссплатформенного компонента. |
| `40_Энциклопедия_Обхода` | `15_Дом/Сети` | Knowledge Source | Синтезированный справочник по методам обхода DPI. |
| `Локализация_dxgettext.md` | `Разработка_Delphi` | References | Инструмент для локализации проектов на Delphi. |

---
*Документ обновляется ИИ при каждом значимом изменении архитектуры или добавлении новых узлов.*
