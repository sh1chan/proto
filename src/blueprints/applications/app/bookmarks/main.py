from flask import Blueprint, render_template


bookmarks = Blueprint(
  'bookmarks', __name__,
  static_folder='static', template_folder='templates/bookmarks'
)


@bookmarks.route('/')
def index():
  return render_template('index.html')
