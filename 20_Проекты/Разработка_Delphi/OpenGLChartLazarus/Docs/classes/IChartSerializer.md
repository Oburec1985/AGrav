---
memory_id: 36395791-142e-4200-8e69-f8eaf7588b16
hash: aeda0bd53658b4dd55fd10d444e6b4b5
last_indexed: '2026-07-07T11:07:51.416475'
---
# IChartSerializer

## Ответственность

Интерфейс сохранения и загрузки модели графика.

## Требование

Сериализатор должен уметь сохранять данные в заданную секцию файла, чтобы не стирать настройки других объектов приложения.

## Layout

При сохранении надо хранить относительную геометрию объектов как главный источник правды. Пиксельные bounds можно не сохранять или сохранять только как вспомогательный cache.

При загрузке:

- читается float-layout;
- модель создается без требования готового OpenGL-контекста;
- пиксельные bounds вычисляются позже, когда известен размер родителя;
- если страница слишком мала, float-layout все равно сохраняет намерение компоновки.

## Реализации

- [TJsonChartSerializer](TJsonChartSerializer.md)
- [TXmlChartSerializer](TXmlChartSerializer.md)

## Связи

- [TChartModel](TChartModel.md)
- [TChartObject](TChartObject.md)
- [TChartLayoutRect](TChartLayoutRect.md)
- [Классовая структура](../architecture.md)
