from flask import Blueprint, render_template


constructor = Blueprint(
  'constructor', __name__,
  static_folder='static/constructor', template_folder='templates',
  static_url_path='/static/constructor'
)


@constructor.route('/', methods=['GET'])
def index():
  return render_template('constructor/index.html')


@constructor.route('/c', methods=['GET', 'POST'])
def constructors():
  return "list of constructors"


@constructor.route('/c/<int:constructor_id>', methods=['GET', 'POST'])
def constructor_by_id(constructor_id: int):
  return f"{constructor_id=}"


@constructor.route('/g', methods=['GET', 'POST'])
def constructor_groups():
  return "list of constructor groups"


@constructor.route('/g/<int:group_id>', methods=['GET'])
def constructor_group_by_id(group_id: int):
  return f"{group_id=}"


@constructor.route('/g/<int:group_id>/<int:constructor_id>', methods=['GET', 'POST'])
def constructor_by_group_id_and_constructor_id(group_id: int, constructor_id: int):
  return f"{group_id=}:{constructor_id=}"
