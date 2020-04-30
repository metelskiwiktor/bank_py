from bank.BankAccount import BankAccount


class BankAccount_INT(BankAccount):

    def __init__(self, ownerName):
        super().__init__(ownerName)
        pass

    @staticmethod
    def instance(accountNumber, balance, accountType, ownerName):
        bank = BankAccount_INT(ownerName)
        return bank.create(accountNumber, balance, accountType, ownerName)
        pass

    def deposit(self, amount):
        balance = self.getBalance() + amount
        self.setBalance(balance)
        pass

    def withdraw(self, amount):
        enoughMoney = super().withdraw(amount)
        if enoughMoney:
            balance = self.getBalance() - amount
            self.setBalance(balance)
        pass
