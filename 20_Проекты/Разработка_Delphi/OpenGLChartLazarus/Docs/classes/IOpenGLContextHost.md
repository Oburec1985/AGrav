---
memory_id: 29bc446b-7c76-4247-a92f-704461ef7af5
hash: 846b2ec36f0d9ffd8d5638ac875d16f1
last_indexed: '2026-07-07T11:07:52.996894'
---
# IOpenGLContextHost

## Ответственность

Интерфейс владельца OpenGL-контекста.

## Зачем нужен

Кроссплатформенность нельзя строить на прямых `HDC/HGLRC`. Контекст должен быть скрыт за переносимой абстракцией, чтобы Windows/Linux-детали не проникали в модель и рендер.

## Методы

- сделать контекст текущим;
- обменять буферы;
- обработать изменение размера.

## Связи

- [TOglChartControl](TOglChartControl.md)
- [TOpenGLChartRenderer](TOpenGLChartRenderer.md)
- [Классовая структура](../architecture.md)
