import os

from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension

from neuralpoet import app

app.debug = True

manager = Manager(app)
toolbar = DebugToolbarExtension(app)


if __name__ == "__main__":
    manager.run()
