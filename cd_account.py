from Account import Account


class CDAccount(Account):
    def __init__(self, balance: float, interest_rate: float, months: int):
        super().__init__(balance, interest_rate, months)
        self.balance = balance
        self.interest_rate = interest_rate
        self.maturity_date = months


def create_cd_account(balance, interest_rate, months):
    account = CDAccount(balance, interest_rate, months)
    interest_earned = (account.balance * (interest_rate / 100)) * (months / 12)
    updated_balance = account.balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest_rate(interest_rate)
    return account.balance, interest_earned
