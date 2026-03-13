from flask import Flask, request, jsonify
import sqlite3
import hashlib
import os

app = Flask(__name__)
DB_PATH = 'security_evolution.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS USER_PLAIN (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        conn.execute('CREATE TABLE IF NOT EXISTS USER_HASH (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password_hash TEXT)')
        conn.commit()

@app.route("/")
def index():
    token = os.getenv("TOKEN_HASH8", "missing_token")
    return f"Hello from Docker! TOKEN_HASH8={token}\n"

@app.route('/signup/v1', methods=['POST'])
def signup_v1():
    data = request.get_json()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO USER_PLAIN (username, password) VALUES (?, ?)', 
                     (data['username'], data['password']))
    return jsonify({"status": "created", "version": "v1_plain"}), 201

@app.route('/login/v1', methods=['POST'])
def login_v1():
    data = request.get_json()
    with sqlite3.connect(DB_PATH) as conn:
        user = conn.execute('SELECT * FROM USER_PLAIN WHERE username=? AND password=?', 
                            (data['username'], data['password'])).fetchone()
    return jsonify({"status": "success" if user else "fail"}), 200

@app.route('/signup/v2', methods=['POST'])
def signup_v2():
    data = request.get_json()
    pw_hash = hashlib.sha256(data['password'].encode()).hexdigest()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO USER_HASH (username, password_hash) VALUES (?, ?)', 
                     (data['username'], pw_hash))
    return jsonify({"status": "created", "version": "v2_hash"}), 201

@app.route('/login/v2', methods=['POST'])
def login_v2():
    data = request.get_json()
    pw_hash = hashlib.sha256(data['password'].encode()).hexdigest()
    with sqlite3.connect(DB_PATH) as conn:
        user = conn.execute('SELECT * FROM USER_HASH WHERE username=? AND password_hash=?', 
                            (data['username'], pw_hash)).fetchone()
    return jsonify({"status": "success" if user else "fail"}), 200

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080, threaded=False)