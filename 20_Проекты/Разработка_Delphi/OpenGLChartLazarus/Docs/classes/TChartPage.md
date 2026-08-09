---
memory_id: b9f013dd-a2c0-447e-a599-8837fac1776b
hash: 65ced40d9cdb7ac838532f3e275c9239
last_indexed: '2026-07-07T11:08:01.678414'
---
# TChartPage

## Ответственность

Логическая область графика и контейнер для вложенных компонентов.

Страница является специализированным [TChartObject](TChartObject.md): у нее есть layout, bounds, дочерние объекты, режимы координат и реакции через frame listeners.

## Содержит

- [TChartViewport](TChartViewport.md);
- список [TChartAxis](TChartAxis.md);
- список [TChartSeries](TChartSeries.md);
- список [TChartCursor](TChartCursor.md);
- список [TChartAnnotation](TChartAnnotation.md);
- вложенные [TChartObject](TChartObject.md), если нужны панели, подстраницы или служебные элементы;
- [TChartLayoutRect](TChartLayoutRect.md) для размещения.

## Размещение

Страница должна хранить и относительное, и пиксельное размещение.

Float-координаты приоритетны при загрузке: они позволяют восстановить расположение даже до создания OpenGL-контекста и до получения реального размера окна. Пиксельные bounds пересчитываются позже, когда родитель уже имеет фактический размер.

При изменении размера экрана страница пересчитывает `PixelRect` из `FloatRect`, а затем пересчитывает дочерние объекты.

## Примагничивание

Страницы должны поддерживать snap-логику:

- примагничивание краев к соседним страницам;
- примагничивание к краям родителя;
- сохранение минимального размера;
- обновление относительных координат после ручного изменения.

Эта логика должна жить не внутри мышиных событий страницы, а в отдельном [IChartFrameListener](IChartFrameListener.md) для layout-режима.

## Пользовательские действия

Страница может реагировать на:

- изменение размера;
- перетаскивание;
- выбор;
- изменение viewport внутри страницы;
- добавление и удаление вложенных объектов;
- пересчет layout при изменении окна.

Реакции выполняются через [TChartFrameListenerList](TChartFrameListenerList.md), чтобы один и тот же объект мог вести себя по-разному в разных режимах.

## Правило

Страница хранит состав графика и геометрию, но не решает, как именно его рисовать. Рендер читает страницу и строит кадр.

## Связи

- [TChartModel](TChartModel.md)
- [TChartViewport](TChartViewport.md)
- [TChartAxis](TChartAxis.md)
- [TChartSeries](TChartSeries.md)
- [TChartObject](TChartObject.md)
- [TChartLayoutRect](TChartLayoutRect.md)
- [IChartFrameListener](IChartFrameListener.md)
- [Классовая структура](../architecture.md)
