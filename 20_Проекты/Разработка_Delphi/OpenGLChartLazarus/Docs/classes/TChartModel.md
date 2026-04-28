# TChartModel

## Ответственность

Корень модели графика. Хранит страницы, стили и общие настройки, которые не зависят от LCL и OpenGL.

## Содержит

- список [TChartPage](TChartPage.md);
- [TChartStyleSet](TChartStyleSet.md);
- состояние обновления `BeginUpdate/EndUpdate`;
- события изменения модели.

## Не делает

- Не рисует.
- Не обрабатывает мышь напрямую.
- Не знает о конкретном OpenGL-контексте.

## Связи

- [TChartPage](TChartPage.md)
- [TChartStyleSet](TChartStyleSet.md)
- [IChartSerializer](IChartSerializer.md)
- [Классовая структура](../Классовая_структура.md)
