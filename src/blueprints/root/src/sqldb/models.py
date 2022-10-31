from src.sql_app import sqldb


"""


Model
  Elements (edits)
  Options

Model edits -> model



Page
  id
  name
  models

  Enum
    Model
      Elements
      Options


Container
  Model (One-to-Many)
    Model_Options

  Model
    Model_Options (One-to-Many)



  Model
    elements (One-to-Many)
    option
"""


class Page(sqldb.Model):
  id = sqldb.Column(sqldb.Integer, primary_key=True)
  name = sqldb.Column(sqldb.String(80), unique=True, nullable=False)
  models = sqldb.relationship('Model')


class Model(sqldb.Model):
  id = sqldb.Column(sqldb.Integer, primary_key=True)
  name = sqldb.Column(sqldb.String(80), unique=True, nullable=False)
  models = sqldb.relationship('Model')




class Model(sqldb.Model):
  __tablename__ = 'model'

  id = sqldb.Column(sqldb.Integer, primary_key=True)
  # TODO: string length
  name = sqldb.Column(sqldb.String(80), unique=True, nullable=False)

  elements_id = sqldb.Column(sqldb.Integer,
                          sqldb.ForeignKey('model_elements_value.id'),
                          nullable=False)
  elements = sqldb.relationship('ModelElementsValue',
                             backref=sqldb.backref('models', lazy=True))

  model_ops_id = sqldb.Column(sqldb.Integer,
                              sqldb.ForeignKey('model_


class Model_Ops(sqldb.Model):
  id = sqldb.Column(sqldb.Integer, primary_key=True)


class Model_Elements(sqldb.Model):
  __tablename__ = 'model_elements'

  id = sqldb.Column(sqldb.Integer, primary_key=True)
  element_id = sqldb.Column(sqldb.Integer)
  element_value = sqldb.Column(
