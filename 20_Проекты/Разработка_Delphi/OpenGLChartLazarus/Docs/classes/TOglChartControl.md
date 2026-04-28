# TOglChartControl

## Ответственность

Главный LCL-компонент, который пользователь кладет на форму Lazarus. Отвечает за интеграцию с LCL, размеры, фокус, входные события и публичный API.

Не хранит данные графика внутри себя: модель живет в [TChartModel](TChartModel.md), отрисовка делегируется [IChartRenderer](IChartRenderer.md), интерактивные режимы - [TChartToolController](TChartToolController.md).

## Реакция на LCL-события

Компонент принимает события LCL и переводит их в контекст графика:

- изменение размера окна;
- mouse down/move/up;
- mouse wheel;
- key down;
- paint/invalidate.

Дальше компонент не решает сам, что именно делать. Он передает события в [TChartToolController](TChartToolController.md), а тот маршрутизирует их через frame listeners.

## Resize

При изменении размера компонент:

- обновляет размер [IOpenGLContextHost](IOpenGLContextHost.md);
- просит renderer обновить viewport;
- сообщает модели, что пиксельные bounds объектов надо пересчитать;
- инициирует перерисовку.

Float-геометрия страниц при этом сохраняется, а пиксельные bounds пересчитываются из нее.

## Не делает

- Не владеет бизнес-моделью точек и серий напрямую.
- Не содержит OpenGL-команды.
- Не сериализует конфигурацию сам.

## Связи

- [TChartModel](TChartModel.md)
- [IChartRenderer](IChartRenderer.md)
- [IOpenGLContextHost](IOpenGLContextHost.md)
- [TChartToolController](TChartToolController.md)
- [TChartLayoutRect](TChartLayoutRect.md)
- [TChartFrameListenerList](TChartFrameListenerList.md)
- [Классовая структура](../Классовая_структура.md)
