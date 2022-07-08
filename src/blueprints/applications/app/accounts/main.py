from flask import (
  Blueprint, request,
  render_template
)

from .src.profile import Profiles
from .src.account import Accounts, AccountOptions


accounts = Blueprint(
  'accounts', __name__,
  static_folder='static', template_folder='templates/accounts'
)


@accounts.route('/', methods=['GET'])
def accounts_and_profiles():
  """Rendering all created profiles
  """
  accounts = Accounts().all()
  profiles = Profiles().all()

  return render_template(
    'accounts_and_profiles.html',
    accounts=accounts, profiles=profiles
  )


# TODO: error handle
# @accounts.route('/profile')
@accounts.route('/profile/<int:profile_id>', methods=['GET', 'POST'])
def profile(profile_id: int = 0):
  """Rendering the profile with it's accounts

  Also rendering the accounts to add to the profile
  """
  # profile = {'personal': {'name': '1'}, 'accounts': []} ??
  profile = Profiles().get(profile_id)
  accounts = Accounts().all()

  return render_template('profile.html', accounts=accounts, profile=profile)


# TODO: error handle
# @accounts.route('/account_options')
@accounts.route('/account_options/<int:account_id>', methods=['GET'])
def account_options(account_id: int = 0) -> dict:
  """Returns account options to render it in the html
  """
  options = AccountOptions().get(account_id)
  return 'options'


# TODO: routes


# TODO: error handle
# @accounts.route('/account', methods=['GET'])
@accounts.route('/account/<int:account_id>', methods=['GET'])
def account(account_id: int = 0) -> None:
  """Account with options
  """
  return 'account'


# TODO: error handle
# @accounts.route('/profile_account', methods=['GET'])
@accounts.route('/profile_account/<int:profile_id>/<int:account_id>', methods=['GET'])
def profile_account(profile_id: int = 0, account_id: int = 0) -> None:
  """Profile account with options
  """
  if profile_id == 0:
    return account(account_id)

  return 'profile_account'
