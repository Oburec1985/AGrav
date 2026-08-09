---
memory_id: ec96ca60-7440-4ee9-8b28-5e1a33187cba
hash: 924916a193c620fe87dd67d93de0c76e
last_indexed: '2026-07-07T11:07:50.387509'
---
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
- [Классовая структура](../architecture.md)
