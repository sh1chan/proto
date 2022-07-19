from flask import Blueprint, render_template


constructor = Blueprint(
  'constructor', __name__,
  static_folder='static/constructor', template_folder='templates',
  static_url_path='/static/constructor'
)


@constructor.route('/', methods=['GET'])
def index():
  return render_template('constructor/index.html')
