# imports
import server.config as conf
from server.views import root
from flask import Flask

# create application
app = Flask(__name__)
app.config.from_object(conf)
app.debug = False

app.register_blueprint(root)
