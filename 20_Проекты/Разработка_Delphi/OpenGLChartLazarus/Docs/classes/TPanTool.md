---
memory_id: 238c801f-aa80-4e0f-b211-484385cd7508
hash: 0ddf19d3af074ff0e14386c9d323faad
last_indexed: '2026-07-07T11:08:11.144390'
---
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
- [Классовая структура](../architecture.md)
