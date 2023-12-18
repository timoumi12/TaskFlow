from api.v1.views import app_views
from flask import request, render_template, session, redirect, url_for
from models import storage
# from flask_session import session
# from models import user

# user_id = session["user_id"]

@app_views.route('/task/<int:task_id>', methods=["GET", "POST", "PUT", "DELETE"])
def task(task_id):
    """manage tasks"""
    print(request.form)
    task_infos = storage.getTaskById(task_id)
    wsp_infos = storage.getWorkspaceById(task_infos.workspace_id)
    if request.method == "POST":
        if request.form.get("action") == "deltask":
            storage.deleteTask(task_id)
            return redirect(url_for('app_views.workspace', workspace_id=wsp_infos.id))
        elif request.form.get("action") == "edittask":
            title = request.form.get("title")
            priority = request.form.get("priority")
            description = request.form.get("description")
            state = request.form.get("state")
            member_id = request.form.get("member")
            edit_data = {"title": title, "priority": priority, "description": description, "state": state, "member_id": member_id}
            print(edit_data)
            storage.editTask(task_id, edit_data)
            return redirect(url_for('app_views.task', task_id=task_infos.id))
    else:
        owner = storage.getUserById(wsp_infos.id_admin)
        member_infos = storage.getUserById(task_infos.member_id)
        uid = session["uid"]
        userWorkspaces = storage.getUserWorkspaces(uid)
        memberOf = userWorkspaces["memberOf"]
        members = storage.getWorkspaceMembers(task_infos.workspace_id)
        return render_template("task.html",
                            task_infos=task_infos,
                            wsp_infos=wsp_infos,
                            owner=owner,
                            member_infos=member_infos,
                            memberOf=memberOf,
                            members=members)

@app_views.route('/update_task_state/<int:task_id>/<string:new_state>', methods=["POST"])
def update_task_state(task_id, new_state):
    task = storage.getTaskById(task_id)
    if task:
        task.state = new_state
        storage.save()
        return "Task state updated successfully"
    else:
        return "Task not found", 404
