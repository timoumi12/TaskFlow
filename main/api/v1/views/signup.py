from flask import redirect, render_template, request, session
from api.v1.views import app_views
#from models.engine.Storage import Storage
from models import storage
from models.users import user
from models.workspaces import workspace
"""signup page"""


@app_views.route("/signup", methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """signup handler"""
    if request.method == "POST":

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confpwd = request.form.get('password_confirm')

        user_data = {"name": name, "email": email, "password": password}
        # test whether the username and pwd fields are present
        if not email or not password or not confpwd:
            return "Must Provide All Fields." #temporary
        # pwd must equal to pwd confirm
        if password != confpwd:
            return "Verify Password."
        # retrieve user
        data = storage.getUserByEmail(email)
        # check user exists
        if data:
            return "This User Already Exists."
        new_user = user(**user_data)
        new_user.save()
        new_user_id = new_user.id
        # Create a private workspace for the new user
        w_name = name.upper() + "_W" + str(new_user_id)
        private_workspace = workspace(id_admin=new_user_id, name=w_name)
        private_workspace.save()
        return redirect("/login")
    else:
        return render_template("signup.html")