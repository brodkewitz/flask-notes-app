import datetime
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import EditNoteForm, ConfirmDeleteNoteForm


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


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    """Edit an existing note"""
    title = "Edit Note"
    if not 0 <= note_id < len(notes):
        flash("No note found with this ID")
        return redirect(url_for('index'))

    form = EditNoteForm()
    if form.validate_on_submit():
        new_note = {
            "date-modified": datetime.datetime.now(),
            "title": form.note_title.data,
            "body": form.note_body.data
        }
        notes[note_id] = new_note
        flash(f"Note updated: {new_note['title']}")
        return redirect(url_for('index'))

    # The form wasn't submitted at this point, so we're going to render
    # the form with the existing note's content.
    # We are preloading the form elements with the note content here,
    # before sending everything over to the template. Normally we would
    # send the note_data over to the template, and use it when rendering
    # the form inputs over there. Unfortunately, WTForms can't
    # currently do that with a `<textarea>`. So instead of e.g.:
    # {{ form.note_title(autofocus="", maxlength="80", value=note_data["title"]) }}
    # ...we're just adding the note data to the form object before it
    # gets sent over. Luckily this works for both kinds of form inputs.
    form.note_title.data = notes[note_id]["title"]
    form.note_body.data = notes[note_id]["body"]

    return render_template("edit.html", title=title, form=form)


@app.route("/delete/<int:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    """Confirm deleting a note"""
    title = "Delete Note"
    if not 0 <= note_id < len(notes):
        flash("No note found with this ID")
        return redirect(url_for('index'))

    form = ConfirmDeleteNoteForm()
    if form.validate_on_submit():
        del notes[note_id]
        flash(f"Note deleted")
        return redirect(url_for('index'))

    return render_template("confirm-delete.html",
                           title=title,
                           note_title=notes[note_id]["title"],
                           form=form)
