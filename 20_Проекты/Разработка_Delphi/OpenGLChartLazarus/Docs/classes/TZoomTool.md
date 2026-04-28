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
- [Классовая структура](../Классовая_структура.md)
