# IChartRenderer

## Ответственность

Интерфейс рендера графика. Отделяет модель и LCL-контрол от конкретной технологии отрисовки.

## Методы

- инициализация;
- изменение размера;
- отрисовка [TChartModel](TChartModel.md);
- чтение bitmap для сохранения изображения.

## Контракт с моделью

Renderer читает модель, но не меняет ее смысловое состояние. Допустимо обновлять временные расчетные данные кадра, если это явно часть layout/render pipeline.

Режим координат объекта должен передаваться через [TChartDrawContext](TChartDrawContext.md), а не через скрытые глобальные флаги.

## Реализации

- [TOpenGLChartRenderer](TOpenGLChartRenderer.md)

## Связи

- [TOglChartControl](TOglChartControl.md)
- [TChartModel](TChartModel.md)
- [TChartDrawContext](TChartDrawContext.md)
- [TChartObject](TChartObject.md)
- [Классовая структура](../Классовая_структура.md)
