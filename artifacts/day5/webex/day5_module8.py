import os
import json
import hashlib
import requests
from pathlib import Path

ARTIFACTS_DIR = Path(__file__).parent

STUDENT_TOKEN = os.getenv("STUDENT_TOKEN", "default_token")
WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
token_hash8 = hashlib.sha256(STUDENT_TOKEN.encode()).hexdigest()[:8]

def save_artifact(name, data):
    with open(ARTIFACTS_DIR / name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def run_webex_tasks():
    if not WEBEX_TOKEN:
        return

    headers = {
        'Authorization': f'Bearer {WEBEX_TOKEN}',
        'Content-Type': 'application/json'
    }
    base_url = 'https://webexapis.com/v1'

    me_resp = requests.get(f'{base_url}/people/me', headers=headers)
    save_artifact("me.json", me_resp.json())

    rooms_resp = requests.get(f'{base_url}/rooms', headers=headers, params={'max': '100'})
    save_artifact("rooms_list.json", rooms_resp.json())

    room_title = f"DevNet_Capstone_{token_hash8}"
    create_room_resp = requests.post(
        f'{base_url}/rooms', 
        headers=headers, 
        json={'title': room_title}
    )
    room_data = create_room_resp.json()
    save_artifact("room_create.json", room_data)
    
    room_id = room_data.get('id')

    if room_id:
        msg_text = f"Automated Lab Message. Hash: {token_hash8}"
        msg_resp = requests.post(
            f'{base_url}/messages',
            headers=headers,
            json={'roomId': room_id, 'text': msg_text}
        )
        save_artifact("message_post.json", msg_resp.json())

        list_msgs_resp = requests.get(
            f'{base_url}/messages',
            headers=headers,
            params={'roomId': room_id}
        )
        save_artifact("messages_list.json", list_msgs_resp.json())

if __name__ == "__main__":
    run_webex_tasks()