# IChartFrameListener

## Ответственность

Интерфейс обработчика пользовательских событий в области графика.

## Идея

Frame listener описывает реакцию на контекст: мышь, клавиатуру, выбранный объект, режим редактирования, drag/resize, изменение viewport. Он может включаться и выключаться без изменения самих объектов.

## Что умеет

- проверить, активен ли listener в текущем контексте;
- принять `MouseDown`, `MouseMove`, `MouseUp`, `MouseWheel`, `KeyDown`;
- выполнить hit-test через базовый [TChartObject](TChartObject.md);
- начать и завершить операцию;
- запросить перерисовку.

## Почему не методы объекта

Один и тот же объект может по-разному реагировать в разных режимах. Например, страница в режиме layout меняет размер, в режиме pan двигает viewport, а в режиме select только выбирается. Это разные listeners, а не разные классы страницы.

## Связи

- [TChartFrameListenerList](TChartFrameListenerList.md)
- [TChartObject](TChartObject.md)
- [TChartToolController](TChartToolController.md)
- [Классовая структура](../Классовая_структура.md)
