---
memory_id: 31299dca-cdc6-4387-a0f6-6ad913deb0cf
hash: b75e812ad55c0b188913cce21ca8fae6
last_indexed: '2026-07-07T11:07:56.476736'
---
# TChartDrawContext

## Ответственность

Контекст отрисовки одного кадра.

## Содержит

- размер окна;
- текущую страницу;
- viewport;
- матрицы или функции преобразования координат;
- текущий режим координат;
- доступ к ресурсам рендера.

## Зачем нужен

Объекты могут рисоваться в координатах родителя, окна или данных. `TChartDrawContext` делает это явным: объект получает контекст и не пытается сам угадать, где находится экран, родитель или viewport.

## Используется

- [TOpenGLChartRenderer](TOpenGLChartRenderer.md);
- [TChartObject](TChartObject.md);
- [TChartViewport](TChartViewport.md).

## Связи

- [TChartObject](TChartObject.md)
- [TOpenGLChartRenderer](TOpenGLChartRenderer.md)
- [TChartViewport](TChartViewport.md)
- [Классовая структура](../architecture.md)
