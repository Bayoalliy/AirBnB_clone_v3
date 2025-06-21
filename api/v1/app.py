#!/usr/bin/python3
"""
entry point
register app_views blueprint
close connection
"""
from flask import Flask
from os import getenv

app = Flask(__name__)
api_host = getenv("HBNB_API_HOST")
api_port = getenv("HBNB_API_PORT")

from models import storage
from api.v1.views import app_views

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_connection(exception):
    """close cureent connection"""
    storage.close()

if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
