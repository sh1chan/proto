from src.sql_app import sqldb


class Constructor(sqldb.Model):
  """Parent

  Pic -> save

  Model
  -----
  """
  __tablename__ = 'constructor'

  id = 0
  name = 'zero'


class ConstructorModels(sqldb.Model):
  """Child (Constructor.ConstructorModels)

  """
  __tablename__ = 'constructor_models'

  id = 0
  constructor_id = 0
  name = 'zero.zero'


class ConstructorModelElements(sqldb.Model):
  """Child (ConstructorModels.ConstructorModelElements)

  """
  __tablename__ = 'constructor_model_elements'

  id = 0
  constructor_models_id = 0
  name = 'zero.zero.zero'



class Models(sqldb.Model):
  pass

class Elements(sqldb.Model):
  pass

class ModelElements(sqldb.Model):
  pass
