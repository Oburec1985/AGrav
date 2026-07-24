---
memory_id: 1e1ae0a4-bc59-41c8-a8b6-f55439961cc9
hash: af1ebc4d8dd0375759543c9666de973b
last_indexed: '2026-07-07T11:08:15.025336'
---
# Заметка: иерархия классов cChart

Первая заметка по Delphi-прототипу `cChart`. Цель - зафиксировать исходную классовую карту до проектирования Lazarus-версии.

Важно: это историческая карта старого компонента, а не целевая архитектура. Новая структура ведется отдельно: [Классовая структура OpenGLChartLazarus](../architecture.md).

Источник анализа:

`C:\Oburec\OburecGH\sharedUtils\компоненты\chart_dpk\chart`

## Главный компонент

```mermaid
classDiagram
    direction TB
    TPanel <|-- cChart
```

`cChart` сейчас совмещает UI-контрол, владельца OpenGL-контекста, менеджер графических объектов, обработчик событий и точку интеграции с редакторскими формами.

## Основная иерархия объектов графика

```mermaid
classDiagram
    direction TB

    cBaseObj <|-- cDrawObj
    cDrawObj <|-- cMoveObj
    cMoveObj <|-- cBoundObj
    cMoveObj <|-- cGraphObj
    cGraphObj <|-- cBasicTrend
    cBasicTrend <|-- cTrend
    cBasicTrend <|-- cBuffTrend1d
    cBasicTrend <|-- cBuffTrend2d
    cGraphObj <|-- cGistogram
    cGraphObj <|-- cPolarGraph
    cPolarGraph <|-- cPolarGraph1d
    cPolarGraph <|-- cPolarGraph1dCycle

    cMoveObj <|-- cLabel
    cLabel <|-- cFloatLabel
    cMoveObj <|-- cTextLabel
    cMoveObj <|-- cYCursor
    cMoveObj <|-- cScrollBar

    cDrawObj <|-- cAxis
    cDrawObj <|-- cBasePage
    cBasePage <|-- cPage
    cPage <|-- cAutoPage
    cBasePage <|-- cGrid
    cBasePage <|-- cEdit
    cEdit <|-- cFloatEdit
    cBasePage <|-- cPolarGraphPage

    cDrawObj <|-- cChartCursor
    cDrawObj <|-- cDoubleCursor
    cDrawObj <|-- cFreqBand
    cDrawObj <|-- cMarkerList
    cDrawObj <|-- cPageMng
    cDrawObj <|-- cPageMngList
    cDrawObj <|-- cDrawObjMng
```

Эта схема собрана по объявлениям `= class(...)` и требует уточнения после чтения методов, владельцев объектов и жизненного цикла.

## Вспомогательные классы

- `cLegend` - легенда, наследуется от `tbtnlistview`.
- `cFontMng` - менеджер шрифтов на базе `TStringList`.
- `cLineLgShader`, `cLineLgShader1d` - shader-слой для отрисовки линий.
- `cClickFrListener`, `cObjFrListener`, `cPageFrListener`, `cCursorFrameListener`, `cDoubleCursorFrameListener` - обработчики событий и интерактивных режимов.

## Формы и редакторы

В прототипе есть набор VCL-форм и фреймов:

- `TChartCfgForm`
- `TEditMenuChartForm`
- `TEditDrawObjFrame`
- `TChartInputFrame`
- `TTrendFrame`
- `TDrawObjFrame`
- `TPageForm`
- `TAxisForm`
- `TCursorForm`
- `TDoubleCursorForm`

Для Lazarus их нельзя считать переносимыми автоматически. Их стоит рассматривать как описание сценариев настройки, а не как готовую UI-архитектуру.

## Риски переноса

- Прямая зависимость от `windows`, `messages`, `HDC`, `HGLRC`.
- Наследование главного компонента от `TPanel`, а не от OpenGL-aware LCL-контрола.
- Смешение модели, рендера и UI-событий в одном классе.
- Возможные зависимости от Delphi-only модулей и старых DCU.
- Кодировка комментариев в исходниках требует отдельной проверки перед переносом.

## Следующие заметки

- Разобрать жизненный цикл `cChart.Create/destroy`, `CreateEngStructs`, `CreateFrameListeners`, `lincEvents`.
- Разобрать объектную модель `cDrawObj`, `cMoveObj`, `cGraphObj`, `cBasicTrend`.
- Разобрать работу страниц `cBasePage`, `cPage`, `cPageMngList`.
- Разобрать OpenGL-контекст и shader-слой.

## Relationships

- [Оглавление](../Оглавление.md) - вход в документацию.
- [Описание](../Описание.md) - зачем переносим компонент.
- [Структура компонента](../architecture.md) - куда раскладываем старую иерархию в новой архитектуре.
- [Классовая структура OpenGLChartLazarus](../architecture.md) - целевая архитектура новой версии.
