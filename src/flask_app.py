from flask import Flask


sh1chan = Flask(__name__)
sh1chan.config.from_object('src.config.DevelopmentConfig')

sh1chan.url_map.strict_slashes = False
