---
memory_id: fde0f90d-0acb-4ea3-810d-a7461191681a
hash: 9ec7fad8a73212fde0ade2e2dfe84cae
last_indexed: '2026-07-07T11:08:04.807740'
---
# TChartViewport

## Ответственность

Преобразование координат между модельным миром графика и экранной областью.

## Содержит

- прямоугольник видимого диапазона данных;
- экранный прямоугольник;
- методы `WorldToScreen` и `ScreenToWorld`.

## Координаты

Viewport не равен layout страницы. Layout отвечает за место страницы в родителе, а viewport отвечает за видимый диапазон данных внутри страницы.

Нужны минимум три преобразования:

- данные -> пиксели страницы;
- пиксели страницы -> данные;
- пиксели окна -> пиксели страницы.

Для объектов со смешанным режимом координат viewport должен уметь преобразовать только одну ось, не трогая вторую.

## Используется

- [TOpenGLChartRenderer](TOpenGLChartRenderer.md) при отрисовке;
- [TPanTool](TPanTool.md) и [TZoomTool](TZoomTool.md) при навигации.
- [IChartFrameListener](IChartFrameListener.md) при обработке мыши.

## Связи

- [TChartPage](TChartPage.md)
- [TChartLayoutRect](TChartLayoutRect.md)
- [TChartDrawContext](TChartDrawContext.md)
- [Классовая структура](../architecture.md)
