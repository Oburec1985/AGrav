---
memory_id: 63628ab7-c537-4437-995c-aa52277efb2f
indexed_at: 2026-06-09 11:52:58.426824
hash: d001192c660d3276eb34372d7f204abb
last_indexed: '2026-07-07T09:42:00.773275'
---
# OglChart — Кроссплатформенный OpenGL-чарт для Lazarus

## Обзор
OglChart — компонент для отображения графиков через OpenGL.  
Создан на Lazarus (FPC 3.2.2), целевая платформа — Windows x64, архитектура рассчитана на кроссплатформу.  
Прототип: Delphi-пакет `chart_dpk`.

## Расположение файлов

| Каталог | Назначение |
|---------|------------|
| `OburecGH\Lazarus\SharedUtils\components\chart_lzr\` | Пакет компонента (основной код) |
| `OburecGH\Lazarus\OGlChartLaz\Test_component\` | Тестовый проект / примеры |
| `OburecGH\sharedUtils\компоненты\chart_dpk\` | Delphi-прототип (для справки) |
| `AGrav\20_Проекты\OglChart\` | Документация |

## Архитектура

### Иерархия объектной модели

```
cBaseObj                       — корень, дерево, имя, сериализация (uOglChartBaseObj)
  └── cDrawObj                 — видимость, цвет, FloatRect (uOglChartDrawObj)
        └── cMoveObj           — выделение, перемещение, resize (uOglChartDrawObj)
              ├── cBasePage    — страница: рамка, фон, отступы, ось X (uOglChartPage)
              ├── cAxis        — ось Y (или X): диапазон, масштаб (uOglChartAxis)
              ├── cBaseTrend   — абстрактный тренд (uOglChartTrend)
              │     └── cLineSeries — массив точек XY
              │           ├── cTrend       — Безье + сплайн
              │           ├── cBuffTrend1d — равномерный буфер (X0, DX)
              │           └── cBuffTrend2d — заготовка
              └── cChart       — корень модели: заголовок, фон, PageArea (uOglChartChart)
```

### Дерево при работе (типичная модель)

```
cChart (корень)
  ├── cBasePage "PageTrend"
  │     └── cAxis "TrendAxisY"
  │           └── cTrend "TrendLine"
  ├── cBasePage "PageSignals"
  │     ├── cAxis "SignalsAxisY"   (синий)
  │     │     └── cLineSeries "SignalBlue"
  │     └── cAxis "Signals2AxisY"  (красный)
  │           └── cLineSeries "SignalRed"
  ├── cBasePage "PageBars"
  │     └── cAxis "BarsAxisY"
  │           └── cBuffTrend1d "BottomBuff1d"
  └── cBasePage "PageOwnX"
        └── cAxis "OwnXAxisY" (UseOwnX=True)
              └── cLineSeries "OwnXLine"
```

### Модули пакета `chart_lzr`

| Модуль | Описание |
|--------|----------|
| `uOglChartTypes` | Интерфейсы: IOpenGLContextHost, IChartRenderer, IChartSerializer, IChartControl |
| `uOglChartLog` | Потокобезопасное логирование в файл (CriticalSection) |
| `uOglChartBaseObj` | `cBaseObj` — базовый узел дерева, менеджер, JSON-точки расширения |
| `uOglChartDrawObj` | `cDrawObj` / `cMoveObj` — визуальные координаты (FloatRect), перемещение |
| `uOglChartPage` | `cBasePage` — страница с рамкой, отступами (PixelTabSpace), осью X |
| `uOglChartAxis` | `cAxis` — ось Y (линейная/лог), опционально своя X |
| `uOglChartTrend` | `cTrend`, `cBuffTrend1d` — тренды: Безье, сплайн, буферный |
| `uOglChartChart` | `cChart` — корень модели, авто-раскладка страниц |
| `uOglChartMng` | `cChartMng` — менеджер: плоский реестр, регистрация дерева |
| `uOglChartRenderer` | `TOpenGLChartRenderer` — OpenGL-рисовалка (~60kB, основной объём) |
| `uOglChartFrameListener` | `TChartFrameListener` — обработка Pan/Zoom/Select/Bezier-edit |
| `uOglChartFontMng` | Менеджер шрифтов (растровый bitmap-font) |
| `uOglChartSerializer` | JSON-сериализатор дерева |
| `uOglChartControl` | `TOglChartControl` — альтернативный контрол с CriticalSection |
| `uoglchart` | `TOglChart` — основной LCL-компонент (Register, Paint, события) |
| `uOglChartModel` | Фасад: uses всех модулей модели (для совместимости) |
| `lzrobrpack` | Пакет LPK — регистрация |

### Тестовый проект (`OGlChartLaz\Test_component`)

| Файл | Описание |
|------|----------|
| `project1.lpi/lpr` | Lazarus-проект, зависимости: LazOpenGLContext, LCL |
| `unit1.pas/lfm` | Главная форма: создание демо-чарта, MouseMove → StatusBar, TreeView |
| `testBaseObj.pas` | Тесты cBaseObj (дерево, AddChild, FindChild и т.д.) |

## Зависимости

- **LCL** — виджеты Lazarus
- **LazOpenGLContext** — OpenGL-контекст для LCL
- **FCL** — Free Component Library (стандарт FPC)
- **fpjson** — JSON (из FPC)
- **SyncObjs** — CriticalSection
- **Windows** — QueryPerformanceCounter (⚠️ не кроссплатформенно!)

## Сборка

```
C:\lazarus\lazbuild.exe "d:\works\OburecGH\Lazarus\OGlChartLaz\Test_component\project1.lpi"
```

Компилятор: `C:\lazarus\fpc\3.2.2\bin\x86_64-win64\fpc.exe`

## Известные проблемы

1. `uoglchart.pas` строка 71: `uses Windows;` — блокирует кроссплатформенность
2. `uOglChartDrawObj.pas` — комментарии в битой кодировке (отображаются мусором)
3. Hint: unit `uBaseObjLaz`, `uBaseObjVclUtils`, `u2DMath` в project1.lpr не используются

## Цветовая модель

Цвета хранятся как `Cardinal` в формате **ABGR** (Alpha-Blue-Green-Red):
- `$FF0000FF` = красный (R=255, G=0, B=0, A=255)
- `$FFFF0000` = синий (R=0, G=0, B=255, A=255)
