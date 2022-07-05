from flask import Blueprint


accounts = Blueprint(
  'accounts', __name__,
  static_folder='static', template_folder='templates/accounts'
)


@accounts.route('/')
def index():
  return '<h1>Accounts</h1>'
