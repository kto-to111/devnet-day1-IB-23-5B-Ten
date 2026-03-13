import json
import os
import subprocess
from pathlib import Path
import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
DAY5_DIR = ROOT / "artifacts" / "day5"
SCHEMA_PATH = ROOT / "schemas" / "day5_summary.schema.json"

def jload(p: Path):
    if not p.exists():
        pytest.fail(f"File not found: {p}")
    return json.loads(p.read_text(encoding="utf-8"))

def test_day5_module8_flow():
    """
    Основной тест 5-го дня: запуск билдера, проверка схемы и контента.
    """
    # 1. Проверка переменных окружения
    env = os.environ.copy()
    assert env.get("STUDENT_TOKEN"), "ОШИБКА: STUDENT_TOKEN не установлен в окружении"
    assert env.get("STUDENT_NAME"), "ОШИБКА: STUDENT_NAME не установлен в окружении"

    # 2. Запуск билдера (src/day5_summary_builder.py)
    builder_script = ROOT / "src" / "day5_summary_builder.py"
    assert builder_script.exists(), "Файл src/day5_summary_builder.py не найден"
    
    result = subprocess.run(
        ["python3", str(builder_script)],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Билдер завершился с ошибкой: {result.stderr}"

    # 3. Проверка существования всех 15 файлов-доказательств
    required_artifacts = [
        "yang/ietf-interfaces.yang",
        "yang/pyang_version.txt",
        "yang/pyang_tree.txt",
        "webex/me.json",
        "webex/rooms_list.json",
        "webex/room_create.json",
        "webex/message_post.json",
        "webex/messages_list.json",
        "pt/external_access_check.json",
        "pt/serviceTicket.txt",
        "pt/network_devices.json",
        "pt/hosts.json",
        "pt/pt_internal_output.txt",
        "pt/postman_collection.json",
        "pt/postman_environment.json"
    ]
    
    for relative_path in required_artifacts:
        full_path = DAY5_DIR / relative_path
        assert full_path.exists(), f"Отсутствует обязательный артефакт: {relative_path}"

    # 4. Валидация по JSON Schema
    summary_path = DAY5_DIR / "summary.json"
    assert summary_path.exists(), "Файл summary.json не был создан"
    
    summary = jload(summary_path)
    schema = jload(SCHEMA_PATH)
    
    try:
        jsonschema.validate(instance=summary, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Ошибка валидации summary.json по схеме: {e.message}")

    # 5. Проверка уникальности данных (Anti-copypaste)
    th8 = summary["student"]["token_hash8"]
    
    # Проверка в Webex (название комнаты)
    room_data = jload(DAY5_DIR / "webex" / "room_create.json")
    assert th8 in room_data.get("title", ""), f"Хэш {th8} не найден в названии комнаты Webex"
    
    # Проверка в Webex (текст сообщения)
    msg_data = jload(DAY5_DIR / "webex" / "message_post.json")
    assert th8 in msg_data.get("text", ""), f"Хэш {th8} не найден в тексте сообщения Webex"

    # Проверка в PT (маркер external access)
    ext_check_text = (DAY5_DIR / "pt" / "external_access_check.json").read_text().lower()
    assert "empty ticket" in ext_check_text, "В external_access_check.json не найден маркер 'empty ticket'"

    # 6. Финальный флаг валидации
    assert summary["validation_passed"] is True, "Флаг validation_passed в summary.json должен быть true"

    print("\n[SUCCESS] Day 5 validation completed. All artifacts verified.")