class Accounts:
  ACCOUNTS = [
    {'id': 1, 'name': 'account_1'},
    {'id': 2, 'name': 'account_2'},
    {'id': 3, 'name': 'account_3'},
  ]

  def all(self) -> None:
    return self.ACCOUNTS


class AccountOptions:

  def get(self, account_id: int) -> None:
    pass
