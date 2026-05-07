from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "mysecretkey"

# ----------------------------
# DATABASE INITIALIZATION
# ----------------------------
def init_db():
    conn = sqlite3.connect("focus.db")
    cursor = conn.cursor()

    # Users table (for authentication)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Data table (for storing names)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------------------------
# HOME PAGE (Protected)
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect("focus.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        return redirect("/")

    conn = sqlite3.connect("focus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    records = cursor.fetchall()
    conn.close()

    return render_template("index.html", data=records)

# ----------------------------
# DELETE DATA
# ----------------------------
@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("focus.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM data WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

# ----------------------------
# REGISTER
# ----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("focus.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
        except:
            conn.close()
            return "Username already exists"

        conn.close()
        return redirect("/login")

    return render_template("register.html")

# ----------------------------
# LOGIN
# ----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("focus.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

# ----------------------------
# LOGOUT
# ----------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)