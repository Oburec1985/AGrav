$source = "c:\Oburec\Antigravity\Projects\temp\РСС"
$dest = "c:\Oburec\Antigravity\Projects\AGrav"

function Move-Safe {
    param($srcRel, $dstRel)
    $srcPath = Join-Path $source $srcRel
    $dstPath = Join-Path $dest $dstRel
    if (Test-Path $srcPath) {
        $parent = Split-Path $dstPath -Parent
        if (!(Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
        Write-Host "[+] Moving $srcRel -> $dstRel"
        Move-Item -Path $srcPath -Destination $dstPath -Force -ErrorAction SilentlyContinue
    } else {
        Write-Host "[!] Not found: $srcRel"
    }
}

# 00_Система
Move-Safe "Инструкции Obsidian" "00_Система/База_Знаний/Obsidian"

# 10_Работа - Датчики
Move-Safe "Модули" "10_Работа/Датчики/Модули"
Move-Safe "Оборудование" "10_Работа/Датчики/Оборудование"
Move-Safe "Тесты/Таблица датчики.md" "10_Работа/Датчики/Таблица_датчики.md"

# 10_Работа - Бизнес Процессы (из Глоссария и корня)
Move-Safe "РСС Книга/Глоссарий/Бизнес процесс ТКП.md" "10_Работа/Бизнес_Процессы/Бизнес_процесс_ТКП.md"
Move-Safe "РСС Книга/Глоссарий/Бизнес процессы.md" "10_Работа/Бизнес_Процессы/Бизнес_процессы.md"
Move-Safe "РСС Книга/Глоссарий/Перечень стендов.md" "10_Работа/Бизнес_Процессы/Перечень_стендов.md"
Move-Safe "РСС Книга/Рабочие/Работа с договорами.md" "10_Работа/Бизнес_Процессы/Работа_с_договорами.md"

# 10_Работа - Экспертиза (ИИ и ДФМ)
Move-Safe "РСС Книга/Проекты/LLM_ИИ" "10_Работа/Экспертиза/ИИ"
Move-Safe "РСС Книга/Проекты/ДФМ (tip-timing и tip clearence).md" "10_Работа/Экспертиза/ДФМ.md"

# 20_Проекты
Move-Safe "ТКП/ЛИАЗ" "20_Проекты/РСС/ЛИАЗ"
Move-Safe "РСС Книга/Рабочие" "20_Проекты/РСС/Рабочие"
Move-Safe "ФБК 3251-ТКП.png" "20_Проекты/РСС/Ассеты/ФБК_3251-ТКП.png"
Move-Safe "ФБК 3251.png" "20_Проекты/РСС/Ассеты/ФБК_3251.png"

# 30_Библиотека
Move-Safe "РСС Книга" "30_Библиотека/Книги/РСС_Книга"

# 90_Архив / Прочее
Move-Safe "Тесты" "90_Архив/РСС_Черновики/Тесты"
Move-Safe "черновики" "90_Архив/РСС_Черновики/черновики"
Move-Safe "README.md" "90_Архив/РСС_Контекст/РСС_README.md"
Move-Safe "Оглавление.md" "90_Архив/РСС_Контекст/РСС_Оглавление.md"
Move-Safe "Оглавление.xlsx" "90_Архив/РСС_Контекст/РСС_Оглавление.xlsx"
Move-Safe "Афоризмы.md" "90_Архив/РСС_Контекст/РСС_Афоризмы.md"
Move-Safe "Pasted image 20250815142753.png" "90_Архив/РСС_Контекст/РСС_Pasted_image.png"

Write-Host "[+] Done."
