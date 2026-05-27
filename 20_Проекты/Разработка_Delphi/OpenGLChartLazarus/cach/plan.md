# План работ: OpenGLChartLazarus

## Сейчас

- [x] Создать папку проекта в AGrav.
- [x] Создать оглавление документации.
- [x] Создать описание проекта.
- [x] Создать первичную структуру компонента.
- [x] Создать первую заметку по иерархии классов `cChart`.
- [x] Зафиксировать решение не копировать архитектуру Delphi-компонента.
- [x] Зафиксировать каталог будущего кода: `e:\Oburec\delphi\2011\OburecGH\Lazarus\SharedUtils\components\chart_lzr\`.
- [x] Создать графическую схему целевой классовой структуры.
- [x] Создать первые страницы описаний классов и связать их со схемой.
- [x] Начать описание layout, bounds, draw modes и frame listeners.

## Ближайшие документационные задачи

- [ ] Уточнить публичный API [TOglChartControl](../Docs/classes/TOglChartControl.md).
- [ ] Уточнить базовый интерфейс [TChartObject](../Docs/classes/TChartObject.md).
- [ ] Уточнить правила размещения [TChartLayoutRect](../Docs/classes/TChartLayoutRect.md).
- [ ] Уточнить модель данных [TChartModel](../Docs/classes/TChartModel.md), [TChartPage](../Docs/classes/TChartPage.md), [TChartSeries](../Docs/classes/TChartSeries.md).
- [ ] Уточнить контракт OpenGL-рендера [IChartRenderer](../Docs/classes/IChartRenderer.md).
- [ ] Уточнить инструменты навигации: [TPanTool](../Docs/classes/TPanTool.md), [TZoomTool](../Docs/classes/TZoomTool.md), [TCursorTool](../Docs/classes/TCursorTool.md), [TSelectTool](../Docs/classes/TSelectTool.md).
- [ ] Уточнить frame listeners: [IChartFrameListener](../Docs/classes/IChartFrameListener.md), [TChartFrameListenerList](../Docs/classes/TChartFrameListenerList.md).
- [ ] Уточнить формат секционной сериализации [IChartSerializer](../Docs/classes/IChartSerializer.md).
- [ ] Разобрать старый Delphi `cChart` как список сценариев и рисков, без копирования структуры.

## Позже, после документации

- [x] Создать Lazarus package.
- [x] Создать демо-приложение.
- [ ] Реализовать минимальный OpenGL viewport.
- [ ] Добавить первую серию данных и оси.
- [ ] Добавить тесты и пример использования.

## Активная фаза: [Слайс 1: Skeleton]

- [x] Реализация базовых интерфейсов (`IOpenGLContextHost`, `IChartRenderer`, `IChartSerializer`)
- [x] Создание LCL-компонента `TOglChartControl` на базе `TOpenGLControl`
- [x] Реализация `TChartModel` с поддержкой JSON-сериализации
- [x] Тестовое приложение с проверкой контекста и сохранения/загрузки
- [x] Пакет `LzrObrPack` собран и установлен в Lazarus IDE; тестовый проект `OGlChartLaz\Test_component\project1.lpi` собирается через `lazbuild -B`.

## Relationships

- [Оглавление документации](../Docs/Оглавление.md)
- [Описание проекта](../Docs/Описание.md)
- [Структура компонента](../Docs/Структура_компонента.md)
- [Классовая структура](../Docs/Классовая_структура.md)
- [Архитектурные размышления](../Docs/Архитектурные_размышления.md)
- [Иерархия классов cChart](../Docs/notes/01_Иерархия_классов_cChart.md)
