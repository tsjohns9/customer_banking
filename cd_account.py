import datetime

from Account import Account


class CDAccount(Account):
    def __init__(self, balance: float, interest_rate: float, months: int):
        super().__init__(balance, interest_rate, months)
        self.balance = balance
        self.interest_rate = interest_rate
        self.start_date = datetime.datetime.now()
        self.maturity_date = months
