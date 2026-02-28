# from flask import Flask, render_template,redirect, url_for
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/default")
# def default():
#     return render_template("home.html", name="Jamie Campbell Bower / vecna", age=30, city="New York")
# @app.route("/default",methods=["POST"])
# def form():
#     a = request.form.get("name")
#     b = request.form.get("email")
#     c = request.form.get("message")
#     return render_template("form.html", name=a, email=b, message=c)
# if __name__ == "__main__":
#     app.run()
# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")  # index than inga form 

# @app.route("/default", methods=["GET", "POST"])
# def default():
#     if request.method == "POST":
#         name = request.form.get("name")
#         age = request.form.get("age")
#         email = request.form.get("email")
#         return render_template("form.html", name=name, age=age, email=email)
#     # return render_template("form.html", name="Jamie Campbell Bower / Vecna", age=30, email="New York")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# from db import get_db_connection

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")
# @app.route("/default", methods=["GET", "POST"])
# def default():
#     if request.method == "POST":
#         name = request.form.get("name")
#         age = request.form.get("age")
#         email = request.form.get("email")
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS students (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER,
#                 email TEXT
#             )
#         """)
#         cursor.execute(
#             "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
#             (name, age, email)
#         )
#         conn.commit()
#         conn.close()
#         return render_template("form.html", name=name, age=age, email=email)
#     return redirect(url_for("home"))  

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, flash
# from db import get_db_connection
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("user.html")  
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     return render_template("login.html")
# @app.route("/display")
# def display():
#     return render_template("home.html")  #main home page
# @app.route("/default", methods=["GET", "POST"])
# def default():
#     if request.method == "POST":
#         name = request.form.get("name")
#         age = request.form.get("age")
#         email = request.form.get("email")
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS students (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER,
#                 email TEXT
#             )
#         """)
#         cursor.execute(
#             "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
#             (name, age, email)
#         )
#         conn.commit()
#         conn.close()
#         flash("Data submitted successfully!", "success")
#         return render_template("form.html", name=name, age=age, email=email)
#     return redirect(url_for("home"))



from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import get_db_connection
from datetime import timedelta
app = Flask(__name__)
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response
app.secret_key = "supersecretkey"
app.permanent_session_lifetime = timedelta(minutes=1)
@app.route("/")
def home():
    return render_template("user.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if "student_name" in session:
        return redirect(url_for("display"))
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        if not name or not age:
            flash("Please enter both name and age!", "danger")
            return redirect(url_for("login"))

        try:
            age = int(age)
        except ValueError:
            flash("Age must be a number!", "danger")
            return redirect(url_for("login"))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                email TEXT
            )
        """)

        cursor.execute("SELECT * FROM students WHERE name = ? AND age = ?", (name, age))
        student = cursor.fetchone()
        conn.close()

        if student:
            session.permanent = True
            session["student_id"] = student[0]
            session["student_name"] = student[1]
            flash("Login successful!", "success")
            return redirect(url_for("display"))
        else:
            flash("Student not found! Please register.", "danger")
            return redirect(url_for("default"))

    return render_template("login.html")


# DISPLAY PAGE (after login)
@app.route("/display")
def display():
    if "student_name" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("login"))

    name = session["student_name"]
    return render_template("home.html", name=name)


# REGISTER
@app.route("/default", methods=["GET", "POST"])
def default():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")

        if not name or not age or not email:
            flash("Please fill all fields!", "danger")
            return redirect(url_for("default"))

        try:
            age = int(age)
        except ValueError:
            flash("Age must be a number!", "danger")
            return redirect(url_for("default"))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                email TEXT
            )
        """)

        cursor.execute("SELECT * FROM students WHERE name = ? AND age = ?", (name, age))
        student = cursor.fetchone()

        if student:
            flash("Student already registered! Please login.", "info")
            conn.close()
            return redirect(url_for("login"))

        cursor.execute(
            "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
            (name, age, email)
        )
        conn.commit()
        conn.close()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("form.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)