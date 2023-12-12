#!/usr/bin/python3
"""homepage.py file"""
from api.v1.views import app_views
from flask import redirect, render_template, request, session
#from models.engine.Storage import Storage
from models import storage
from models.workspaces import workspace
from models.users import user
from api.v1.helpers import login_required


@app_views.route("/home", methods=["GET", "POST"], strict_slashes=False)
@login_required
def index():
    if request.method == "GET":
        uid = session["uid"]
        wsp = session["wsp"]
        # we'd be using this to display username
        userAttributes = storage.getUserById(uid)
        # retrieve all workspaces to display them in the sidebar by name/(id?)
        userWorkspaces = storage.getUserWorkspaces(uid)
        # workspaces that the user is invited to
        memberOf = userWorkspaces["memberOf"]
        # workspaces that the user owns (created them)
        owned = userWorkspaces["owned"]
        # the one and only private workspace
        private = userWorkspaces["private"]
        # if wsp == "private":
        #     tasks = storage.getPrivateTasks(uid)
        # else :
        #     tasks = storage.getWorkspaceTask(wsp)
        # just for display
        # print(userAttributes.id, userAttributes.name)
        # print("\n###\n###\n###")
        # # just for display too, meaning we'd be using this loop int the front end to display workspaces in the sidebar
        # for wspace in userWorkspaces:
        #     print(wspace.id, "  µµµµ  ", wspace.code)
        return render_template("homepage.html",
                               private=private,
                               user_id=uid,
                               user_name=userAttributes.name,
                               owned=owned,
                               memberOf=memberOf,
                               )
    elif request.method == "POST":
        action = request.form.get("action")
        uid = session["uid"]
        if action == "addworksp":
            # get workspace name
            wspace_name = request.form.get("name")
            new_workspace = workspace(id_admin=uid, name=wspace_name)
            new_workspace.save()
            return "workspace added."
        elif action == "joinworksp":
            current_user = storage.getUserById(uid)
            code = request.form.get("code")
            #print(code)
            target_wsp = storage.getWorkspaceByCode(code)
            #print(target_wsp)
            print(current_user.workspaces)
            current_user.workspaces.append(target_wsp)
            print(current_user.workspaces)
            current_user.save()
            return "joined successfully."
