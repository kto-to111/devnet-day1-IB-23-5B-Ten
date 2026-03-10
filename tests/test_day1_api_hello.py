import json
import os
import sys
import subprocess
from pathlib import Path
import jsonschema
import pytest

# Пути относительно корня проекта
ROOT = Path(__file__).resolve().parents[1]
ART_DIR = ROOT / "artifacts" / "day1"
SUMMARY = ART_DIR / "summary.json"
SCHEMA = ROOT / "schemas" / "day1_summary.schema.json"

def test_day1_artifacts_and_schema():
    """Основной тест: запуск скрипта и проверка выходных данных."""
    
    # 1. Подготовка команды запуска
    cmd = [sys.executable, "src/day1_api_hello.py"]
    
    # Если response уже есть, можно добавить --offline, но для теста лучше чистый прогон
    # cmd.append("--offline") 

    # 2. Проверка наличия переменных окружения (внутри теста)
    env = os.environ.copy()
    assert "STUDENT_TOKEN" in env, "STUDENT_TOKEN must be set"
    assert "STUDENT_NAME" in env, "STUDENT_NAME must be set"
    assert "STUDENT_GROUP" in env, "STUDENT_GROUP must be set"

    # 3. Запуск скрипта через subprocess
    r = subprocess.run(cmd, cwd=str(ROOT), env=env, capture_output=True, text=True)
    
    # Проверяем код возврата (0 - успех, 2 - ошибка валидации API)
    assert r.returncode in (0, 2), f"Скрипт упал с ошибкой:\n{r.stderr}"

    # 4. Проверка наличия файлов
    assert SUMMARY.exists(), "Файл summary.json не создан!"
    assert SCHEMA.exists(), "Файл схемы не найден в schemas/!"

    # 5. Валидация JSON по схеме
    summary_data = json.loads(SUMMARY.read_text(encoding="utf-8"))
    schema_data = json.loads(SCHEMA.read_text(encoding="utf-8"))

    jsonschema.validate(instance=summary_data, schema=schema_data)

    # 6. Проверка логики
    assert summary_data["api"]["status_code"] == 200, "API вернул не 200 OK"
    assert summary_data["api"]["validation_passed"] is True, "Валидация данных API не прошла"
    assert len(summary_data["api"]["response_sha256"]) == 64, "Хэш должен быть длиной 64 символа"