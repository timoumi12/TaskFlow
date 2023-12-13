from api.v1.views import app_views
from flask import jsonify
from models import storage
# from flask import session


# workspace_id = session['workspace_id'] 
@app_views.route('/users')
def users():
    """get all users"""

