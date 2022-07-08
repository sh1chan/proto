class Profiles:
  PROFILES = [
    {'id': 1, 'name': 'profile_1'},
    {'id': 2, 'name': 'profile_2'},
    {'id': 3, 'name': 'profile_3'},
  ]

  PROFILE_ACCOUNTS = {
    1: {'accounts': [{'id': 1, 'name': 'account_1'}, {'id': 2, 'name': 'account_2'}],},
    2: {'accounts': [{'id': 1, 'name': 'account_1'}, {'id': 2, 'name': 'account_2'},
                     {'id': 3, 'name': 'account_3'},],}
  }

  def all(self) -> None:
    return self.PROFILES

  def get(self, profile_id: int) -> None:
    return self.PROFILE_ACCOUNTS.get(profile_id)
