import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    target = request.args.get('target', '')
    result = subprocess.Popen(f"ping -c 4 {target}", shell=True, stdout=subprocess.PIPE)
    return result.stdout.read()

@app.route('/user', methods=['GET'])
def get_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    user_id = request.args.get('id', '') 
    query = f"SELECT * FROM users WHERE id = '{user_id}'"  
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return str(user)

@app.route('/read', methods=['GET'])
def read_file():
    filename = request.args.get('file', '')
    with open(f"/var/www/{filename}", "r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
