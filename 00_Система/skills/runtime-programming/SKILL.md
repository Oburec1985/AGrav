---
name: runtime-programming
description: >-
  Cross-project RunTime / hot-path rules for threaded and real-time code:
  no allocations after start, cache structure pointers instead of string
  lookups, process arrays with bulk/SIMD-friendly ops instead of per-sample
  loops. Use when editing worker threads, acquisition loops, timers that
  publish data, DSP/streaming paths, SetLength/new/malloc in loops, FindByName
  / dictionary lookups by string each tick, or when the user mentions RunTime,
  hot path, or preallocated buffers — in any language or project, not only
  RecorderLnx.
---

# RunTime Programming

Универсальные правила для **любого** проекта (Delphi/Lazarus, C/C++, C#,
Python native extensions, DSP, сетевые воркеры). Источник норм AGrav:
`00_Система/Код_Стандарты.md`,
`10_Работа/Программирование/Методологии/Потоки_и_Память.md`.

Канон для Cursor: `C:\Users\User\.cursor\skills\runtime-programming\SKILL.md`.

## Три главных запрета

1. **Не выделять память в RunTime.** Делать это при инициализации или
   переконфигурировании. В горячем пути работать в заранее выделенных буферах.
2. **Не искать по строкам в RunTime.** Предпочитать готовые ссылки/указатели/
   индексы на структуры, собранные на этапе конфигурации.
3. **Не делать поточечные операции без нужды.** Обрабатывать массивы блоками —
   `Move`/memcpy, векторные/аппаратно ускоренные функции, batch API — вместо
   цикла «на каждый отсчёт / каждый элемент».

## Когда это RunTime

Считается RunTime (hot path), если код крутится **после старта рабочей фазы**:
worker-thread, цикл опроса, callback приёма пакета, audio/DSP process,
high-rate timer публикации данных, lock-free очередь «данные готовы».

**Не RunTime** (аллокации и поиск по имени допустимы): загрузка конфига, UI OK,
wizard, `Init`/`Configure`/`Reconfigure`/`Prepare`/`Start` до первого тика.

## Правила (обобщённо)

### Память

- Запрещены в hot path: `SetLength`, `Create`/`new`, `GetMem`/`malloc`,
  `realloc` вниз/вверх каждый тик, сборка строк, рост контейнеров
  (`push_back` без reserve, `TStringList.Add` без ёмкости).
- Выделять по **априорным** данным: max каналов, max размер блока, max клиентов.
- **Clear > Recreate**: очищать и переиспользовать объекты; не ломать внешние ссылки.
- Если resize неизбежен: только **вверх**, Capacity не уменьшать в RunTime,
  лучше один крупный chunk, чем N мелких alloc.

### Ссылки вместо строк

- На Configure/Start построить таблицы: `имя → указатель`, `индекс канала → record*`,
  `id → handle`.
- В тике: только индекс / pointer / handle. Запрещены повторные
  `FindByName`, `IndexOf`, линейный обход списка по `SameText`, JSON parse,
  rebuild настроек из конфига.
- Смена конфига → Stop или явный Reconfigure вне опроса → пересборка кэша.

### Массивы вместо точек

- Равномерный сигнал: хранить `x0` + `dx` + массив `Y`, не разворачивать ось X
  на каждый отсчёт в acquisition (это работа визуализации/шейдера).
- Линейные преобразования (`y = a*x + b`), копирование, fill, sum — блочными
  примитивами / SIMD / профильной math-библиотекой проекта.
- Поэлементный цикл — только если операция принципиально скалярная
  (нелинейная таблица без векторизации) и это осознанный fallback.

### Потоки и побочные эффекты

- Состояние потока менять **только из самого потока**; снаружи — команды.
- Предпочитать critical sections; Events — осторожно (сложнее отлаживать).
- Не писать синхронный лог/диск на каждый элемент/канал в hot path.
- UI не дёргать на каждый блок: очередь + таймер/throttle.

### Конфиг и нотификации

- Снимок настроек собирать **один раз** при Program/Start/Reconfigure.
- Уведомления — **пачкой** («блок готов» / «кадр N»), не N× поиск + N× notify.

## Чеклист перед сдачей hot-path правки

```
- [ ] Нет alloc/resize контейнеров в цикле тика
- [ ] Буферы выделены на Init/Configure/Start
- [ ] Нет поиска по строке/имени в тике — только кэш ссылок
- [ ] Нет лишнего поэлементного цикла там, где возможен block/SIMD/Move
- [ ] Нет rebuild конфига / JSON в тике
- [ ] Нотификации не размножены без нужды
- [ ] UI/лог не на каждый sample
- [ ] Сборка/тесты проекта OK
```

## Фазы жизненного цикла

| Фаза | Можно | Нельзя |
|------|--------|--------|
| Load / UI / Configure | Create, FindByName, JSON, SetLength(max) | — |
| Prepare / Reconfigure / Start | кэш указателей, финальный resize | горячий цикл опроса |
| RunTime (тик / callback) | Fill, Move, арифметика в готовых буферах | alloc, string lookup, rebuild config |
| Stop / Shutdown | освобождение, hold busy | долгие probe без нужды |

## Примеры анти-паттернов (любой стек)

| Плохо в RunTime | Хорошо |
|-----------------|--------|
| `SetLength`/`new[]` каждый кадр | буфер с Capacity ≥ max |
| `registry.FindByName(channelName)` | `fChannels[i].Tag` pointer |
| `for j: times[j] = t0 + j*dt` | передать `(t0, dt, count)` |
| `for j: y[j] = convert(x[j])` при линейной ГХ | `scale_add(y, x, a, b, n)` |
| notify × N с поиском имени | один event «block ready» |
| parse JSON / rebuild settings в тике | кэш record на Start |

Конкретный разбор RecorderLnx/MIC-185 (иллюстрация):
`D:\works\OburecGH\Lazarus\RecorderLnx\Docs\mic185-runtime-audit-2026-07-24.md`

## Если без alloc никак

1. Resize только вверх при `need > Capacity`.
2. Не ужимать Capacity в RunTime.
3. Один большой буфер лучше множества мелких.
4. Зафиксировать причину в проектном `errors/` или заметке.

## Relationships

- [[Код_Стандарты]]
- [[Потоки_и_Память]]
