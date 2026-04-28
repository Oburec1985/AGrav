# TChartToolController

## Ответственность

Диспетчер интерактивных режимов и frame listeners.

## Содержит

- активный [IChartTool](IChartTool.md);
- список [TChartFrameListenerList](TChartFrameListenerList.md);
- маршрутизацию событий мыши и клавиатуры;
- общий контекст операции: модель, страница, viewport, выбранные объекты.

## Frame listeners

Инструмент задает общий режим, а конкретные реакции выполняют listeners. Например, режим layout включает listeners изменения размеров страниц и snap-логики, а режим просмотра включает pan/zoom.

Listener может отказаться от события, и тогда событие идет следующему listener по приоритету.

## Инструменты

- [TPanTool](TPanTool.md)
- [TZoomTool](TZoomTool.md)
- [TCursorTool](TCursorTool.md)
- [TSelectTool](TSelectTool.md)

## Связи

- [TOglChartControl](TOglChartControl.md)
- [IChartTool](IChartTool.md)
- [IChartFrameListener](IChartFrameListener.md)
- [TChartFrameListenerList](TChartFrameListenerList.md)
- [Классовая структура](../Классовая_структура.md)
