#!/usr/bin/python3
"""logout.py file"""
from api.v1.views import app_views
from flask import redirect, session


@app_views.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")