# План работ RecorderLnx

## Текущий этап

Документационное проектирование и перенос функциональной модели Windows Recorder в кроссплатформенную Lazarus-архитектуру Windows/Linux без COM.

## Ближайшие задачи

- [x] Создать документацию проекта в AGrav.
- [x] Зафиксировать первую карту интерфейсов Windows Recorder.
- [x] Выбрать физическое расположение исходников RecorderLnx: `D:\works\OburecGH\Lazarus\RecorderLnx\`.
- [x] Создать skeleton Lazarus/FPC проекта.
- [x] Извлечь рабочие идеи из руководства пользователя Recorder и скорректировать план.
- [x] Согласовать и реализовать минимальную модель `TRecorderStateMachine` по руководству Recorder: `Stop`, `PreviewArmed`, `Preview`, `RecordArmed`, `Record`, условия старта.
- [x] Сделать пример/тест для `TRecorderStateMachine`.
- [x] Обновить карту классов после первой реализации.

## Принцип выполнения задач

Один класс или крупный блок за раз: код, пример использования, проверка, запись в документацию.
- [ ] Перед каждым кодовым шагом задавать пользователю наводящие вопросы и фиксировать согласованное решение до реализации.


## 2026-05-25

- Skeleton создан как кроссплатформенное LCL-приложение Windows/Linux: RecorderLnx.lpi, RecorderLnx.lpr, UI/uMainForm.pas, UI/uMainForm.lfm, Core/.
- Windows-сборка skeleton проверена через `C:\lazarus\lazbuild.exe`; прямой `fpc` не найден в PATH, но Lazarus использует встроенный компилятор.

- Добавлен .gitignore проекта RecorderLnx для build-артефактов lib/, backup и Pascal object/unit файлов.


## После изучения PDF Recorder

- Состояние View в документации и коде дальше называть Preview/Просмотр, если пользователь не решит иначе.
- Перед state machine согласовать модель ожидания старта по TTL/уровню/времени: отдельное состояние или фаза внутри Preview/Record.
- В архитектуре учитывать сущности Замер/Кадр, Рабочий каталог, Измерительный канал, ГХ, КХ, Триггер, Уставка, Формуляр отображения, Плагин.
- Ближайший кодовый шаг не расширять до всей конфигурации Recorder; сначала сделать маленькую, но правильную модель режимов и условий перехода.


## TRecorderStateMachine

- TRecorderStateMachine реализован в D:\works\OburecGH\Lazarus\RecorderLnx\Core\uRecorderStateMachine.pas.
- Тест-пример: D:\works\OburecGH\Lazarus\Tests\RecorderTests\StateMachine\RecorderStateMachineTest.lpr.
- Проверено: C:\lazarus\lazbuild.exe D:\works\OburecGH\Lazarus\RecorderLnx\RecorderLnx.lpi; C:\lazarus\fpc\3.2.2\bin\x86_64-win64\fpc.exe ... RecorderStateMachineTest.lpr; запуск RecorderStateMachineTest.exe.
- Следующий кодовый шаг перед реализацией согласовать отдельно: подключение state machine к UI или первая модель конфигурации/каналов.

## Порядок ближайших работ после state machine

Принята последовательность: ядро -> минимальный интерфейс наблюдения состояния -> инструменты настройки/тестовые примеры -> сохранение/загрузка конфигурации -> полноценный интерфейс настройки.

- [x] Ядро: выделить настройки запуска/остановки в отдельную модель `TRecorderRunControlSettings`.
- [x] Тестовые примеры: расширить `RecorderStateMachineTest` несколькими сценариями разных условий старта/остановки.
- [x] Конфигурация: добавить сохранение/загрузку настроек запуска/остановки после стабилизации модели.
- [x] Минимальный UI наблюдения состояния: подключить state machine к LCL-форме для отображения текущего режима и простого журнала событий без интерфейса настройки.
- [ ] Полноценный UI настройки: делать после проверки ядра, тестовых примеров и конфигурации.

## Стандарт документации кода

- [x] Документировать код новых units: аннотация в начале модуля, назначение функций и параметров, комментарии для нетривиальной логики.
- [ ] Привести uRecorderStateMachine.pas к этому стандарту.

- uRecorderStateMachine.pas документирован по стандарту: шапка unit, пояснения типов, методов, параметров и ключевой логики переходов. Сборка проекта и теста после правки прошла успешно.

## Производительность и аппаратное ускорение

- [ ] Перед реализацией расчетных блоков проверять `D:\works\OburecGH\sharedUtils\math\uHardwareMath.pas` и существующие OpenGL-наработки в AGrav/проектах.
- [ ] Для тяжелых операций сначала сделать корректный тест-пример и измерение, затем выбирать SIMD/OpenGL/другой ускоренный путь.
- [ ] Для ускоренных модулей предусматривать кроссплатформенный fallback Windows/Linux.

## TRecorderRunControlSettings

- TRecorderRunControlSettings реализован в D:\works\OburecGH\Lazarus\RecorderLnx\Core\uRecorderRunControlSettings.pas.
- Принятые параметры: один класс, Rising/Falling, DelayMs, канал строкой, уровень Double.
- Тест-пример расширен: manual, start by signal level, delayed start, stop by duration, stop by signal level, ошибки при отсутствии имени канала.
- Проверено: сборка RecorderLnx.lpi, сборка и запуск RecorderStateMachineTest.exe.
- Следующий шаг по порядку: сохранение/загрузка конфигурации для TRecorderRunControlSettings.


## Конфигурация TRecorderRunControlSettings

- Добавлены SaveToFile и LoadFromFile в TRecorderRunControlSettings.
- Формат первой версии: INI с разделами Start и Stop; enum-значения хранятся стабильными строками.
- Тест-пример расширен round-trip проверкой сохранения/загрузки.
- Проверено: сборка RecorderLnx.lpi, сборка и запуск RecorderStateMachineTest.exe.
- Следующий шаг по порядку: после ядра, примеров и конфигурации можно начинать аккуратное подключение к визуальному интерфейсу либо согласовать следующий core-объект, если UI еще рано.

## Безопасное обновление файлов

- [x] Зафиксировать правило: после правок сверять рабочий файл, backup-дубликаты, `LastWriteTime` и при риске запускать принудительную сборку `-B`.
- [x] Для `uRecorderRunControlSettings.pas` восстановлена рабочая версия из backup, обновлен timestamp, выполнены `lazbuild -B`, `fpc -B` и запуск теста.

## Уточнение порядка UI

- Минимальный интерфейс, который позволяет видеть состояние ядра, делается до/рядом с тестовыми примерами: индикатор состояния, журнал, простые команды Preview/Record/Stop.
- Интерфейс настройки параметров запуска/остановки остается в конце, после ядра, примеров и сохранения/загрузки.


## Минимальный UI наблюдения состояния

- TMainForm теперь владеет TRecorderStateMachine, показывает текущий режим и журнал переходов.
- Команды формы: Preview, Record, Trigger, Stop. Интерфейс настройки параметров не добавлялся.
- Рабочие файлы проверены по ключевым строкам и timestamp; выполнена принудительная сборка lazbuild -B.
- Следующий шаг по порядку: продолжить инструменты/тестовые примеры или согласовать следующий core-блок перед UI настройки.

## UI по скриншоту Recorder

- [x] Зафиксировать UI-ориентир из скриншота Recorder в AGrav.
- [x] Перестроить минимальный UI: верхние вкладки формуляров, центральная область, правый пульт состояния/команд, поиск и список тегов-заглушек.
- [x] Подключить `Record` к `TRecorderRunControlSettings.StartCondition`; `Preview` оставить ручным.
- [ ] Добавить dev-структуру `config\app.ini` и `config\projects\default\run-control.ini`.

## UI-каркас Recorder

- Главная форма перестроена по ориентирам скриншота Recorder: верхняя панель формуляров, центральная таблица, правый пульт, поиск/список тегов, журнал.
- Preview оставлен ручным; Record использует TRecorderRunControlSettings.StartCondition.
- Добавлены файлы config/app.ini и config/projects/default/run-control.ini.
- Settings пока placeholder; следующий UI-шаг - отдельный подробный диалог настройки, когда согласуем состав.
- Проверено: рабочие файлы сверены по ключевым строкам, Memo1 удален, выполнена принудительная сборка lazbuild -B.

## Правка UI-пульта и вынос тестовых данных

- Settings и Save перенесены из верхней панели формуляров в правый пульт команд рядом со Stop/View/Rec.
- Кнопки правого пульта переведены на иконки-символы с Hint; текстовые подписи сохранены только как подсказки.
- Индикатор состояния и времени стал цветным: Stop - серый, armed/preview - желтый, Record - зеленый.
- `InitPlaceholderData` удален из `uMainForm`; временное наполнение формуляра и списка тегов вынесено в `Tests\RecorderTests\UITestData\uRecorderUiTestData.pas`.
- Зафиксировано правило: стандартный язык передачи данных компонентам Recorder - теги; устройства и плагины пишут в теги, компоненты отображают их через notify.
- Проверено: `lazbuild -B RecorderLnx.lpi`, `fpc -B RecorderStateMachineTest.lpr`, запуск `RecorderStateMachineTest.exe`.


## Glyph-иконки правого пульта

- Кнопки `Settings`, `Save`, `Stop`, `View`, `Record`, `Trigger` заменены с `TButton` на `TSpeedButton`.
- Unicode-символы убраны из `Caption`; иконки создаются как маленькие bitmap `Glyph` в `TMainForm.AssignCommandGlyph`.
- Проверено: исходники компилируются; основной `RecorderLnx.exe` был заблокирован Windows после запуска, поэтому контрольная линковка выполнена во временный `RecorderLnx_check.exe`.

## ImageList и Record -> Preview

- На главную форму добавлен компонент `ilCommandButtons: TImageList`; иконки правого пульта добавляются в него и затем назначаются на `TSpeedButton.Glyph`.
- Исправлен переход state machine: из `rsRecord` можно перейти в `rsPreview` командой просмотра.
- Зафиксирована модель кадра записи: каталог на диске с номером `0001`, `0002`, ...; при `Record -> Preview` текущий каталог записи завершается, следующая запись создает новый каталог.
- Проверено: сборка теста `RecorderStateMachineTest`, запуск теста, контрольная сборка приложения в `RecorderLnx_check.exe`.

## Design-time ImageList правого пульта

- `ilCommandButtons` теперь не пустой в дизайнере Lazarus: изображения лежат в `uMainForm.lfm` в свойстве `Bitmap` самого `TImageList`.
- Кнопки `Settings`, `Save`, `Stop`, `View`, `Record`, `Trigger` привязаны к списку через `Images = ilCommandButtons` и `ImageIndex = 0..5`.
- Runtime-генерация иконок из `SetupCommandButtons` удалена; код формы только задает `Caption`, `Hint` и поведение.
- Проверено: `lazbuild -B RecorderLnx.lpi`, запуск `RecorderStateMachineTest.exe`.
