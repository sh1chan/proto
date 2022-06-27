from flask import Blueprint


root = Blueprint('root', __name__, static_folder='static', template_folder='templates')
