#!/usr/bin/python3
"""homepage.py file"""

from api.v1.views import app_views
from flask import render_template


@app_views.route("/", methods=["GET"], strict_slashes=False)
def indexxyz():
    """returns the Project Landing Page"""
    return render_template('index.html')