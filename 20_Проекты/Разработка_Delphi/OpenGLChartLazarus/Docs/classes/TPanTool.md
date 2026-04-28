# TPanTool

## Ответственность

Инструмент перемещения видимой области графика.

## Работает с

- [TChartViewport](TChartViewport.md);
- активной [TChartPage](TChartPage.md).

## Правило

Меняет только viewport, не меняет данные серий.

Если активен layout-режим страницы, перемещение страницы должен выполнять другой listener. Это важно: pan данных и перемещение страницы внешне похожи мышью, но меняют разные координатные системы.

## Связи

- [IChartTool](IChartTool.md)
- [IChartFrameListener](IChartFrameListener.md)
- [TChartViewport](TChartViewport.md)
- [Классовая структура](../Классовая_структура.md)
