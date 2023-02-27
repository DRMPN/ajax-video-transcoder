import os
import subprocess
from tempfile import mkdtemp

from cs50 import SQL
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from flask_session import Session
from werkzeug.exceptions import HTTPException, InternalServerError, default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from helpers import apology, login_required

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")
ALLOWED_EXTENSIONS = "webm"

# Configure upload folder
UPLOAD_FOLDER = "./uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

# Configure upload url
app.add_url_rule("/uploads/<name>", endpoint="download_file", build_only=True)


@app.route("/hello", methods=["GET"])
def hello():
    """Show Login/Register form"""
    if not session:
        return render_template("hello.html")
    else:
        return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            flash("Username field can't be blank", "danger")
            return render_template("hello.html")
        if not request.form.get("password") or not request.form.get("confirmation"):
            flash("Password field can't be blank", "danger")
            return render_template("hello.html")
        username_db_query = db.execute(
            "SELECT username FROM users WHERE username = ?",
            request.form.get("username"),
        )
        if len(username_db_query) == 0:
            if request.form.get("password") == request.form.get("confirmation"):
                flash("Registered!", "success")
                db.execute(
                    "INSERT INTO users (username, hash) VALUES (?,?)",
                    request.form.get("username"),
                    generate_password_hash(request.form.get("password")),
                )
            else:
                flash("Passwords do not match", "danger")
                return render_template("hello.html")
        else:
            flash("Username is already exists", "danger")
            return render_template("hello.html")
        return render_template("hello.html")


@app.route("/login", methods=["POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            flash("Must provide username", "danger")
            return render_template("hello.html")
        elif not request.form.get("password"):
            flash("Must provide password", "danger")
            return render_template("hello.html")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username and/or password", "danger")
            return render_template("hello.html")

        session["user_id"] = rows[0]["id"]

        return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")


@app.route("/")
@login_required
def index():
    """Show upload form"""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
@login_required
def upload():
    if not request.files.get("file").filename:
        flash("No file to upload", "danger")
        return redirect("/")
    else:
        file = request.files["file"]
        if not allowed_file(file.filename):
            flash("Only WebM extension is allowed", "danger")
            return redirect("/")
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        flash("File is processing!", "success")
        filepath_new = filepath.rsplit(".webm")[0]
        filename_new = filename.rsplit(".webm")[0] + ".mp4"
        cmd = f"ffmpeg -y -hide_banner -loglevel error -fflags +genpts -i {filepath} -r 24 {filepath_new}.mp4"
        res = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        _, err = res.communicate()
        if err != b"":
            flash(f"Error: {err}", "danger")
            return redirect("/")
        flash("File is ready!", "success")
        return render_template(
            "index.html", loadurl=url_for("download_file", name=filename_new)
        )


@app.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def allowed_file(filename):
    """Check if fileformat is allowed"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=8080)
