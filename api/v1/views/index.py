#!/usr/bin/python3
"""
creates an endpoint that checks api status.
Return: json
"""
from api.v1.views import app_views
import json


@app_views.route('/status', strict_slashes=False)
def view_status():
    dic = {'status': 'OK'}
    return json.dumps(dic)
