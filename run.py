#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from src.blueprints.root.main import root
from src.blueprints.applications.main import applications


sh1chan = Flask(__name__)
sh1chan.config.from_object('src.config.DevelopmentConfig')

sh1chan.url_map.strict_slashes = False

sh1chan.register_blueprint(root, url_prefix='/')
sh1chan.register_blueprint(applications, url_prefix='/applications')


if __name__ == '__main__':
  sh1chan.run()
