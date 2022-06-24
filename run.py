#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


sh1chan = Flask(__name__)
sh1chan.config.from_object('src.config.DevelopmentConfig')


if __name__ == '__main__':
  sh1chan.run()
