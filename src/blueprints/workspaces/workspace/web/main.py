from flask import Blueprint


web = Blueprint(
  'web', __name__,
  static_folder='static/web', template_folder='templates',
  static_url_path='/static/web'
)


@web.route('/')
def index():
  return '<h1>Web</h1>'
