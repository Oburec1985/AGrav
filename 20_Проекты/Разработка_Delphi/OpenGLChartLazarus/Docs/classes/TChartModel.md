---
memory_id: 4e072a13-aa6b-4a22-aa4d-1465754ae892
hash: 791469ccd9860014408d3c81d8470400
last_indexed: '2026-07-07T11:07:58.978205'
---
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
- [Классовая структура](../architecture.md)
