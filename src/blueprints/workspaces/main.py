from flask import Blueprint

from .workspace.web.main import web


workspaces = Blueprint('workspaces', __name__, static_folder='static')

workspaces.register_blueprint(web, url_prefix='/web')


@workspaces.route('/')
def index():
  return '<h1>Workspaces</h1>'
