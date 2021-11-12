from datetime import datetime

from app import db
from app.models import Note


if __name__ == '__main__':
    # Create the database
    db.create_all()

    # Populate it with the same notes from our original variable
    initial_notes = [
        Note(
            date_modified=datetime(2021, 10, 1, 15, 2),
            title="Shoes return address",
            body="56 Runway Pl.\nDover, DE 19904",
        ),
        Note(
            date_modified=datetime(2021, 10, 3, 10, 19),
            title="Hard boiled egg method",
            body="Bring water to a boil first. Water level should be below the top of the eggs so that they won't be completely submerged. Leave room around the eggs so they don't bump into each other, or they'll get pebble textured and be very hard to peel.",
        ),
        Note(
            date_modified=datetime(2021, 10, 12, 8, 30),
            title="Bacon ipsum",
            body="Pancetta duis id excepteur ground round adipisicing consequat laboris porkbelly turkey shoulder, landjaeger occaecat ad laborum tri-tip shortloin tenderloin ham hamburger consectetur, drumstick nisi shortribs dolore elit sint qui shankle sed chicken, deserunt cow fugiat venison sausage labore in veniam commodo.\n\nFrankfurter dolore id mollit buffalo consequat ham hock burgdoggen corned beef elit, rump lorem spareribs shank ullamco reprehenderit exercitation qui shoulder, chuck dolor ham bresaola doner adipisicing excepteur deserunt, ball tip kielbasa labore do landjaeger venison aute tempor.",
        ),
        Note(
            date_modified=datetime(2021, 10, 18, 19, 37),
            title="New lock code room 202",
            body="12345",
        )
    ]

    # db.session is a transaction in SQL terminology
    # Collect our notes into the current transaction "queue"
    for note in initial_notes:
        db.session.add(note)

    # Commit our changes to the database all at once. Sometimes we need
    # to make multiple changes to a database, like updating multiple
    # tables. Sometimes if the changes are not all saved successfully it
    # could leave the database in a broken state. By using sessions
    # (transactions), we can queue up all of our changes, then commit
    # them all at once. This way the whole transaction either succeeds
    # and the database is fully updated correctly, or it fails and the
    # database is left unaffected.
    db.session.commit()
