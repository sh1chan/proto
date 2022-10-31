from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .databse import Base


class Account(Base):
  __tablename__ = "account"

  id = Column(Integer, primary_key=True)
  ico = Column(String)
  name = Column(String, nullable=False)


class AccountOptions(Base):
  __tablename__ = "account_options"

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  account_id = Column(Integer)

  profile_accounts_id = Column(Integer, ForeignKey("profile_accounts.id"))


class ProfileAccounts(Base):
  __tablename__ = "profile_accounts"

  id = Column(Integer, primary_key=True)
  account_options = relationship("AccountOptions")
