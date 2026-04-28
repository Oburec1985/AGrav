# TOpenGLChartRenderer

## Ответственность

OpenGL-реализация [IChartRenderer](IChartRenderer.md).

## Содержит

- ссылку на [IOpenGLContextHost](IOpenGLContextHost.md);
- [TChartDrawContext](TChartDrawContext.md) для текущего кадра;
- подготовку OpenGL-состояния;
- отрисовку страниц, осей, серий, курсоров и подписей;
- чтение изображения из framebuffer.

## Режимы рисования

Renderer должен уважать режим координат каждого [TChartObject](TChartObject.md):

- координаты родителя;
- координаты окна;
- координаты данных;
- смешанный режим.

Это важно для страниц, курсоров, подписей, оверлеев и служебных элементов. Объект сообщает намерение через draw/coordinate mode, а renderer применяет нужные преобразования.

## Bounds

Перед отрисовкой renderer не должен вычислять всю компоновку с нуля. Он использует уже рассчитанные пиксельные bounds модели, а при необходимости просит объект обновить bounds через общий интерфейс.

## Не делает

- Не создает LCL-окно.
- Не владеет моделью.
- Не меняет данные серий.

## Связи

- [IChartRenderer](IChartRenderer.md)
- [IOpenGLContextHost](IOpenGLContextHost.md)
- [TChartModel](TChartModel.md)
- [TChartObject](TChartObject.md)
- [TChartDrawContext](TChartDrawContext.md)
- [Классовая структура](../Классовая_структура.md)
