from api.v1.views import app_views
from flask import jsonify
from models import storage
# from flask_session import session
# from models import user

# user_id = session["user_id"]

@app_views.route('/workspace/<int:workspace_id>')
def workspace(workspace_id):
    """manage workspace"""
    tasks = storage.getWorkspaceTask(workspace_id)

# @app_views.route('/workspaces/{workspace_id}')
# def workspace(workspace_id):
#     """get a workspace"""
#     a_workspace = storage.get(workspace, workspace_id)
#     session['workspace_id'] = a_workspace
#     return jsonify(a_workspace)
