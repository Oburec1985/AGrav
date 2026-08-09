---
memory_id: 6ddbaae3-31d0-4318-84fd-d8177286cbe8
hash: 94450a828d0e05227e86d889e97a1d32
last_indexed: '2026-07-07T11:08:13.244645'
---
# TZoomTool

## Ответственность

Инструмент масштабирования графика.

## Режимы

- масштаб колесом мыши;
- масштаб прямоугольником;
- сброс масштаба к данным.

## Работает с

- [TChartViewport](TChartViewport.md);
- границами [TChartSeries](TChartSeries.md).

## Контекст

Zoom меняет viewport данных внутри страницы. Он не меняет layout страницы. Если пользователь тянет край страницы, это событие должен забрать layout listener до zoom listener.

## Связи

- [IChartTool](IChartTool.md)
- [IChartFrameListener](IChartFrameListener.md)
- [TChartViewport](TChartViewport.md)
- [Классовая структура](../architecture.md)
