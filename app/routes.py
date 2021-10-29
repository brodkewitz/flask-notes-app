from flask import render_template
from app import app


notes = [
    {
        "date-modified": "10/1/21 3:02pm",
        "title": "Shoes return address",
        "body": "56 Runway Pl.\nDover, DE 19904",
    },
    {
        "date-modified": "10/3/21 10:19am",
        "title": "Hard boiled egg method",
        "body": "Bring water to a boil first. Water level should be below the top of the eggs so that they won't be completely submerged. Leave room around the eggs so they don't bump into each other, or they'll get pebble textured and be very hard to peel.",
    },
    {
        "date-modified": "10/12/21 8:30am",
        "title": "Bacon ipsum",
        "body": "Pancetta duis id excepteur ground round adipisicing consequat laboris porkbelly turkey shoulder, landjaeger occaecat ad laborum tri-tip shortloin tenderloin ham hamburger consectetur, drumstick nisi shortribs dolore elit sint qui shankle sed chicken, deserunt cow fugiat venison sausage labore in veniam commodo.\n\nFrankfurter dolore id mollit buffalo consequat ham hock burgdoggen corned beef elit, rump lorem spareribs shank ullamco reprehenderit exercitation qui shoulder, chuck dolor ham bresaola doner adipisicing excepteur deserunt, ball tip kielbasa labore do landjaeger venison aute tempor.",
    },
    {
        "date-modified": "10/18/21 7:37pm",
        "title": "New lock code room 202",
        "body": "12345",
    },
]


@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title, notes=notes)


@app.route("/edit")
def edit_note():
    """Create a new note or edit an existing one"""
    title = "New Note"

    return render_template("edit.html")
