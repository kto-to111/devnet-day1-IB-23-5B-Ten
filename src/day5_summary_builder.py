#!/usr/bin/env python3
import hashlib
import json
import os
import sys
import platform
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SUMMARY_SCHEMA_VERSION = "5.0"

def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]

def dump_json(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")

def read_text_safe(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()

def read_json_safe(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

def hash_file_safe(path: Path) -> str:
    if not path.exists():
        return ""
    return sha256_text(path.read_text(encoding="utf-8"))

def main() -> int:
    st_token = os.getenv("STUDENT_TOKEN", "").strip()
    st_name = os.getenv("STUDENT_NAME", "").strip()
    st_group = os.getenv("STUDENT_GROUP", "").strip()
    
    if not st_token or not st_name or not st_group:
        print("ERROR: set STUDENT_TOKEN, STUDENT_NAME, STUDENT_GROUP", file=sys.stderr)
        return 1

    th8 = token_hash8(st_token)
    
    # --- Выполнение логических проверок (Checks) ---
    pyang_tree_text = read_text_safe(ART / "yang" / "pyang_tree.txt")
    pyang_tree_ok = "+--rw interfaces" in pyang_tree_text
    
    room_create = read_json_safe(ART / "webex" / "room_create.json")
    webex_room_ok = th8 in room_create.get("title", "")
    
    message_post = read_json_safe(ART / "webex" / "message_post.json")
    webex_message_ok = th8 in message_post.get("text", "")
    
    ext_access_text = read_text_safe(ART / "pt" / "external_access_check.json")
    pt_empty_ticket = "empty ticket" in ext_access_text.lower()
    
    net_devices = read_json_safe(ART / "pt" / "network_devices.json")
    hosts = read_json_safe(ART / "pt" / "hosts.json")
    pt_version_ok = net_devices.get("version") == "1.0" or hosts.get("version") == "1.0"
    
    validation_passed = pyang_tree_ok and webex_room_ok and webex_message_ok and pt_empty_ticket and pt_version_ok

    # --- Сбор хешей всех обязательных артефактов ---
    evidence_files = {
        "ietf_interfaces": ART / "yang" / "ietf-interfaces.yang",
        "pyang_version": ART / "yang" / "pyang_version.txt",
        "pyang_tree": ART / "yang" / "pyang_tree.txt",
        
        "webex_me": ART / "webex" / "me.json",
        "webex_rooms_list": ART / "webex" / "rooms_list.json",
        "webex_room_create": ART / "webex" / "room_create.json",
        "webex_message_post": ART / "webex" / "message_post.json",
        "webex_messages_list": ART / "webex" / "messages_list.json",
        
        "pt_ext_access": ART / "pt" / "external_access_check.json",
        "pt_service_ticket": ART / "pt" / "serviceTicket.txt",
        "pt_network_devices": ART / "pt" / "network_devices.json",
        "pt_hosts": ART / "pt" / "hosts.json",
        "pt_internal_output": ART / "pt" / "pt_internal_output.txt",
        "pt_postman_collection": ART / "pt" / "postman_collection.json",
        "pt_postman_environment": ART / "pt" / "postman_environment.json",
    }
    
    evidence_sha256 = {k: hash_file_safe(v) for k, v in evidence_files.items()}

    # --- Формирование итогового словаря (как в Day 4) ---
    summary = {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "generated_utc": now_utc(),
        "student": {
            "token": st_token,
            "token_hash8": th8,
            "name": st_name,
            "group": st_group
        },
        "checks": {
            "pyang_tree_ok": pyang_tree_ok,
            "webex_room_ok": webex_room_ok,
            "webex_message_ok": webex_message_ok,
            "pt_empty_ticket": pt_empty_ticket,
            "pt_version_ok": pt_version_ok
        },
        "evidence_sha256": evidence_sha256,
        "validation_passed": validation_passed,
        "run": {
            "python": platform.python_version(),
            "platform": sys.platform
        }
    }

    # Сохраняем в файл и выводим в консоль
    dump_json(summary, ART / "summary.json")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())