from flask import Blueprint, render_template


accounts = Blueprint(
  'accounts', __name__,
  static_folder='static', template_folder='templates/accounts'
)


@accounts.route('/')
def index():
  return render_template('index.html')
