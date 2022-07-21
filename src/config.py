# SEE: https://flask.palletsprojects.com/en/2.1.x/config/#configuration-basics

class Config:
  DEBUG = False
  TESTING = False

  SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/test.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
