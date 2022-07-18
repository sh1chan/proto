from flask import Blueprint, render_template


web = Blueprint(
  'web', __name__,
  static_folder='static/web', template_folder='templates',
  static_url_path='/static/web'
)


@web.route('/', methods=['GET'])
def index():
  return render_template('web/index.html')
