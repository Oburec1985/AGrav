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
- [Классовая структура](../Классовая_структура.md)
