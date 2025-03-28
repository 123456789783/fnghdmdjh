from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

DB_FILE = "database.db"
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE NOT NULL,password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

init_db()
@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        c = conn.cursor()
        
        try:
            cursor.exucute('INSERT into USERS')
        
# Main function that starts the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)