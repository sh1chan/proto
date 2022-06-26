from flask import Blueprint

from .app.bookmarks.main import bookmarks


applications = Blueprint('applications', __name__, static_folder='static')

applications.register_blueprint(bookmarks, url_prefix='/bookmarks')


@applications.route('/')
def index():
  return '<h1>Applications</h1>'
