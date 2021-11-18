import os


# Note: Tried pathlib but ran into trouble with the database uri when
# SQLAlchemy tries to parse it.
# basedir = Path(__file__).parent
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess fallback string'
    # Heroku sets a DATABASE_URL environment variable, but SQLAlchemy
    # doesn't like the url protocol name that is uses. We can fix this
    # up with a simple string replacement.
    if 'DATABASE_URL' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace(
            'postgres://', 'postgresql://')
    else:
        # If the environment variable isn't set, assume we're offline
        # and use the sqlite database.
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
