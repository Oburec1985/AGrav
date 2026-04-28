# TChartFrameListenerList

## Ответственность

Список frame listeners и диспетчер их приоритетов.

## Что умеет

- хранить набор [IChartFrameListener](IChartFrameListener.md);
- включать и выключать listeners по контексту;
- определять, кто первым получает событие;
- передавать событие дальше, если listener его не обработал;
- сбрасывать активную операцию при смене режима.

## Контекстные примеры

- режим layout: активны listeners изменения размера страниц и примагничивания;
- режим просмотра: активны pan/zoom listeners;
- режим курсоров: активен listener перемещения курсоров;
- режим редактирования объектов: активны select/drag/resize listeners.

## Связи

- [IChartFrameListener](IChartFrameListener.md)
- [TChartToolController](TChartToolController.md)
- [TOglChartControl](TOglChartControl.md)
- [Классовая структура](../Классовая_структура.md)
