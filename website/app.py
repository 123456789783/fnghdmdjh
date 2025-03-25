from flask import Flask, render_template, jsonify, request, redirect
import sqlite3
import json
import os

app = Flask(__name__)

DB_FILE = "database.db"

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.commit()
        conn.close()

init_db()

@app.route("/")
def website():
    return render_template("website.html")

# Main function that starts the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)