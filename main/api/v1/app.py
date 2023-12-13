from api.v1.views import app_views
from flask import Flask, make_response, jsonify, session
from flask_session import Session
from flask_cors import CORS
from models.base import Base


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "alxTaskflow"
Session(app)
app.register_blueprint(app_views)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')