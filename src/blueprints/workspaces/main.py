from flask import Blueprint

from .workspace.constructor.main import constructor


workspaces = Blueprint('workspaces', __name__, static_folder='static')

workspaces.register_blueprint(constructor, url_prefix='/constructor')


@workspaces.route('/')
def index():
  return '<h1>Workspaces</h1>'
