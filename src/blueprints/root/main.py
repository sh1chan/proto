from flask import Blueprint


root = Blueprint(
  'root', __name__,
  static_folder='static/root', template_folder='templates',
  static_url_path='/static/root'
)
