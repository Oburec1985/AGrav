---
memory_id: 89e9395e-2013-431d-8d2b-967258797258
hash: 0c511d08fa0a8325c13dfcdc6808e933
last_indexed: '2026-07-07T11:08:04.038008'
---
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
- [Классовая структура](../architecture.md)
