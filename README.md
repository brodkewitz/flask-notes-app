# Flask-Notes app

A sample dynamic web application built with Flask.

Created 2021-10-18

**Warning:** This repo could receive force pushed updates as I rewrite, clean up, tag and annotate the git history. Clone or fork at your own risk!


To run the app:

- Clone or download the repo

- Create a virtual environment

    ```
    $ cd flask-notes-app/
    $ python3 -m venv venv
    ```

- pip install requirements

    ```
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```

- Set environment variables

    ```
    $ export FLASK_APP=flask-notes-app.py
    $ export FLASK_ENV=development
    ```

- Create the sqlite database

    ```
    $ python3 init-db.py
    ```

- Run the app

    ```
    $ flask run
    ```
