from bank.BankAccount_COVID19_firma import BankAccount_COVID19_firma


class BankService:
    # notPossibleToClose = BankAccount_COVID19_firma.__class__.__name__ //i dont know why but it returns ABCMeta
    notPossibleToClose = "BankAccount_COVID19_firma"

    def __init__(self, banks) -> None:
        self.__banks = banks
        pass

    def deposit(self, accountNumber, amount):
        bank = self.bank(accountNumber)
        if self.__noticeIfNone(bank):
            return

        self.bank(accountNumber).deposit(amount)
        pass

    def withdraw(self, accountNumber, amount):
        bank = self.bank(accountNumber)
        if self.__noticeIfNone(bank):
            return

        bank.withdraw(amount)
        pass

    def close(self, accountNumber):
        bank = self.bank(accountNumber)
        if self.__noticeIfNone(bank):
            return

        if self.notPossibleToClose == bank.getAccountType():
            print("U cannot close this account because it's " + self.notPossibleToClose)
            return
        del self.__banks[accountNumber]
        pass

    def bank(self, accountNumber):
        for bank in self.__banks.values():
            if accountNumber == bank.getAccountNumber():
                return bank
        pass

    def __noticeIfNone(self, bank):
        if bank is None:
            print("Provided account number isn't valid")
            return True
        return False
        pass

    def print(self):
        for bank in self.__banks.values():
            print(bank)
        pass

    def getBanks(self):
        return self.__banks
        pass
