from flask import render_template
from app import app


@app.route("/")
def hello_world():
    title = "Home"
    return render_template("index.html", title=title)
