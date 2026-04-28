# IChartTool

## Ответственность

Интерфейс интерактивного инструмента графика.

Инструмент задает пользовательский режим: просмотр, layout, курсоры, выбор, редактирование. Конкретные реакции внутри режима выполняются frame listeners.

## События

- `MouseDown`;
- `MouseMove`;
- `MouseUp`;
- при необходимости `KeyDown`.

## Реализации

- [TPanTool](TPanTool.md)
- [TZoomTool](TZoomTool.md)
- [TCursorTool](TCursorTool.md)
- [TSelectTool](TSelectTool.md)

## Отношение к frame listeners

`IChartTool` не обязан сам обрабатывать каждое движение мыши. Он может включить нужные [IChartFrameListener](IChartFrameListener.md) в [TChartFrameListenerList](TChartFrameListenerList.md).

Например, layout-tool включает listeners изменения размера страницы, перетаскивания страницы и snap-логики.

## Связи

- [TChartToolController](TChartToolController.md)
- [IChartFrameListener](IChartFrameListener.md)
- [TChartFrameListenerList](TChartFrameListenerList.md)
- [Классовая структура](../Классовая_структура.md)
