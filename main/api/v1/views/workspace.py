from api.v1.views import app_views
from flask import request, render_template, session
from models import storage
# from flask_session import session
# from models import user

# user_id = session["user_id"]

@app_views.route('/workspace/<int:workspace_id>', methods=["GET", "POST", "PUT", "DELETE"])
def workspace(workspace_id):
    """manage workspace"""
    wsp_infos = storage.getWorkspaceById(workspace_id)
    tasks = storage.getWorkspaceTask(workspace_id)
    uid = session["uid"]
    userWorkspaces = storage.getUserWorkspaces(uid)
    memberOf = userWorkspaces["memberOf"]
    if request.method == "POST":
        title = request.form.get('title')
        member_id = request.form.get('member_id')
        priority = request.form.get('priority')
        description = request.form.get('description')
        task_data = {"title": title, "member_id": member_id, "priority": priority, "description": description}
        storage.addTask(**task_data)
    else:
        # retrieve the members of the specific workspace
        members = storage.getWorkspaceMembers(workspace_id)
        return render_template("workspace.html",
                               wsp_infos=wsp_infos,
                               tasks=tasks,
                               members=members,
                               memberOf=memberOf)

# @app_views.route('/workspaces/{workspace_id}')
# def workspace(workspace_id):
#     """get a workspace"""
#     a_workspace = storage.get(workspace, workspace_id)
#     session['workspace_id'] = a_workspace
#     return jsonify(a_workspace)
