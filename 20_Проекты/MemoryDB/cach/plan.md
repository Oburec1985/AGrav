# План разработки проекта MemoryDB

## Задачи:
1. [x] Создать структуру папок и requirements.txt.
2. [x] Реализовать src/config.py с путями и настройками.
3. [x] Реализовать src/embeddings.py с генерацией ONNX-эмбеддингов.
4. [x] Реализовать src/database.py с локальным клиентом Qdrant.
5. [x] Реализовать src/main.py с логикой MCP-сервера.
6. [x] Создать тестовый скрипт src/test_local.py.
7. [x] Создать скрипты run_memory_server.bat и run_test.bat.
8. [x] Добавить документацию в docs/README.md и docs/architecture.md.
9. [x] Установить зависимости Python.
10. [x] Выполнить тестовый запуск src/test_local.py и проверить корректность работы.
11. [x] Задокументировать результаты работы в cach/notes_last_state.md.
12. [x] Добавить .gitignore для игнорирования бинарных файлов базы данных и кэша моделей.
13. [x] Добавить RECORDS_DIR в src/config.py.
14. [x] Реализовать _sync_with_disk() и обновить сохранение/удаление в src/database.py.
15. [x] Протестировать корректность синхронизации с диском через run_test.bat.
16. [x] Документировать концепцию разделения памяти и связь с Obsidian (YAML) в docs/architecture.md.
17. [x] Создать системный промпт/инструкцию docs/llm_memory_instructions.md для LLM.
18. [x] Создать скрипт автоматической очистки src/cleanup.py и run_cleanup.bat.
19. [x] Протестировать работу скрипта очистки и процесс разметки заметок.
20. [x] Объединить папки документации OglChart и OpenGLChartLazarus, устранив дублирование.
21. [x] Проиндексировать в MemoryDB файлы RecorderLnx и OpenGLChartLazarus с разметкой YAML Frontmatter.
22. [x] Оценить экономию токенов при использовании векторного поиска.
