from flask import redirect, render_template, request, session
from api.v1.views import app_views
#from models.engine.Storage import Storage
from models import storage
from models.users import user
"""login page"""


@app_views.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """login handler"""
    # Clear any previous session
    session.clear()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # test whether the username and pwd fields are present
        if not email or not password:
            return "Must Provide All Fields" #temporary
        # retrieve user
        data = storage.getUserByEmail(email)
        # check user exists
        if data is None:
            return "User Exists Not"
        # store user in session
        session["uid"] = data.id
        # indicate that the user will have his private workspace as the default one as soon as they login
        session["wsp"] = "private"
        print(session)
        return redirect("/home")
    else:
        return render_template("login.html")
