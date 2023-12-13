from flask import Blueprint, session


app_views = Blueprint('app_views', __name__, url_prefix='')
from api.v1.views.user import *
from api.v1.views.task import *
from api.v1.views.workspace import *
from api.v1.views.homepage import *
from api.v1.views.login import *
from api.v1.views.signup import *
from api.v1.views.index import *