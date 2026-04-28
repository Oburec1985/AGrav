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
- [Классовая структура](../Классовая_структура.md)
