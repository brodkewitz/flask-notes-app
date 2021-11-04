import datetime
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import EditNoteForm


notes = [
    {
        "date-modified": datetime.datetime(2021, 10, 1, 15, 2),
        "title": "Shoes return address",
        "body": "56 Runway Pl.\nDover, DE 19904",
    },
    {
        "date-modified": datetime.datetime(2021, 10, 3, 10, 19),
        "title": "Hard boiled egg method",
        "body": "Bring water to a boil first. Water level should be below the top of the eggs so that they won't be completely submerged. Leave room around the eggs so they don't bump into each other, or they'll get pebble textured and be very hard to peel.",
    },
    {
        "date-modified": datetime.datetime(2021, 10, 12, 8, 30),
        "title": "Bacon ipsum",
        "body": "Pancetta duis id excepteur ground round adipisicing consequat laboris porkbelly turkey shoulder, landjaeger occaecat ad laborum tri-tip shortloin tenderloin ham hamburger consectetur, drumstick nisi shortribs dolore elit sint qui shankle sed chicken, deserunt cow fugiat venison sausage labore in veniam commodo.\n\nFrankfurter dolore id mollit buffalo consequat ham hock burgdoggen corned beef elit, rump lorem spareribs shank ullamco reprehenderit exercitation qui shoulder, chuck dolor ham bresaola doner adipisicing excepteur deserunt, ball tip kielbasa labore do landjaeger venison aute tempor.",
    },
    {
        "date-modified": datetime.datetime(2021, 10, 18, 19, 37),
        "title": "New lock code room 202",
        "body": "12345",
    },
]


@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title, notes=notes)


@app.route("/new", methods=["GET", "POST"])
def new_note():
    """Create a new note"""
    title = "New Note"
    form = EditNoteForm()
    # validate_on_submit() only tries to validate on POST, so we don't
    # have to check which method was used for the request.
    if form.validate_on_submit():
        new_note = {
            "date-modified": datetime.datetime.now(),
            "title": form.note_title.data,
            "body": form.note_body.data
        }
        notes.append(new_note)
        flash(f"New note created: {new_note['title']}")
        return redirect(url_for('index'))

    return render_template("edit.html", title=title, form=form)
