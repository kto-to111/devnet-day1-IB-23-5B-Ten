# Day 1 Report — DevNet Sprint

## 1. Student
- **Name:** Тен Владимир Александрович
- **Group:** IB-23-5b
- **GitHub repo:** https://github.com/kto-to111/devnet-day1-IB-23-5B-Ten
- **Day1 Token:** D1-IB-23-5b-24-0A7D

## 2. NetAcad progress (Module 1)
- **Completed items:** 1.1 / 1.2 / 1.3 (Основы DevNet и API)

## 3. VM evidence
- **File:** `artifacts/day1/env.txt` exists: **Yes**

## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : **Yes**
- `tests/test_day1_api_hello.py` : **Yes**
- `schemas/day1_summary.schema.json` : **Yes**
- `artifacts/day1/summary.json` : **Yes**
- `artifacts/day1/response.json` : **Yes**

## 5. Commands run (paste EXACT output)
### 5.1 Script run
```text
{
  "api": {
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe",
    "status_code": 200,
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "validation_errors": [],
    "validation_passed": true
  },
  "generated_utc": "2026-03-10T10:40:53.436906+00:00",
  "run": {
    "platform": "linux",
    "python": "3.8.2"
  },
  "schema_version": "1.0",
  "student": {
    "group": "IB-23-5b",
    "name": "Тен Владимир Александрович",
    "token": "D1-IB-23-5b-24-0A7D"
  }
}
```

### 5.2 Tests
```text
(.venv) devasc@labvm:~/Desktop/day1/devnet-day1-IB-23-5B-Ten$ pytest -q
.                                                                                                                                                                                     [100%]
1 passed in 0.53s
```
## 6. What I learned today (3–6 bullets)
* Изучил работу с переменными окружения в Linux и их корректную загрузку из `.env` файлов через `source`.
* Понял важность детерминированной сериализации JSON (использование `sort_keys=True`) для обеспечения идентичности хэша SHA256.
* Научился автоматизировать запуск и проверку Python-скриптов с помощью библиотеки `pytest` и модуля `subprocess`.
* Отработал навыки создания артефактов (логов и JSON-отчетов) в рамках CI/CD подхода.
* Попрактиковался в валидации данных API на соответствие эталонным значениям и схемам.

## 7. Problems & fixes (at least 1)
**Problem:**
При попытке экспорта данных через команду `export $(grep -v '^#' .env | xargs)` возникала ошибка `bash: export: not a valid identifier`. Это происходило из-за того, что `xargs` разбивал ФИО студента по пробелам, и Bash пытался интерпретировать каждое слово как отдельную переменную. Также тесты не запускались из-за отсутствия `import sys` в файле тестов.

**Fix:**
Для загрузки переменных использовал более надежный метод:
```bash
set -a
source .env
set +a