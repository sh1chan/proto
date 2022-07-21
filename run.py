#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from src.flask_app import sh1chan
from src.blueprints.root.main import root
from src.blueprints.applications.main import applications
from src.blueprints.workspaces.main import workspaces


sh1chan.register_blueprint(root, url_prefix='/')
sh1chan.register_blueprint(applications, url_prefix='/applications')
sh1chan.register_blueprint(workspaces, url_prefix='/workspaces')


if __name__ == '__main__':
  sh1chan.run()
