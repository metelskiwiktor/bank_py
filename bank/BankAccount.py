import uuid
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, ownerName):
        self.__accountNumber = uuid.uuid4().hex
        self.__balance = 0
        self.__accountType = self.__class__.__name__
        self.__ownerName = ownerName

    def create(self, accountNumber, balance, accountType, ownerName):
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__accountType = accountType
        self.__ownerName = ownerName
        return self
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        pass

    def getOwnerName(self) -> str:
        return self.__ownerName
        pass

    def getAccountNumber(self) -> str:
        return self.__accountNumber
        pass

    def getAccountType(self):
        return self.__accountType

        pass

    def getBalance(self) -> int:
        return self.__balance
        pass

    def setBalance(self, balance):
        self.__balance = balance
        pass

    def __str__(self) -> str:
        return "account number: " + self.__accountNumber + \
               "\nbalance: " + format(self.__balance) + \
               "\naccount type:" + self.getAccountType() + \
                "\nowner name: " + self.__ownerName

    def __iter__(self):
        return iter([self.__accountNumber, self.__balance, self.__accountType, self.__ownerName])
