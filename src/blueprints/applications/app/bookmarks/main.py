from flask import Blueprint


bookmarks = Blueprint('bookmarks', __name__, static_folder='static')


@bookmarks.route('/')
def index():
  return '<h1>Bookmarks</h1>'
