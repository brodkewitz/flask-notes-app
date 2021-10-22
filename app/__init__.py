from flask import Flask


# There are two kinds of "app" here, which is confusing.

# "app" variable is our instance of the Flask class. This gets imported
# by all of our other modules in the application. This "app" is part of
# the package.
app = Flask(__name__)

# "from app" here refers to the whole package, as named by this file's
# parent directory. Putting our "import" statements down here is a
# workaround to avoid circular imports, because there are two things
# called "app". All of the other modules in our application must import
# the Flask app variable above. Putting imports at the bottom here
# allows all the modules to have their imports at the top. Yup, it's
# confusing.
from app import routes
