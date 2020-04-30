from bank.BankAccount_COVID19 import BankAccount_COVID19
from bank.BankAccount_COVID19_firma import BankAccount_COVID19_firma
from bank.BankAccount_INT import BankAccount_INT

from bank.BankService import BankService


def main():
    global banksMap
    bankAccount1 = BankAccount_COVID19("wiktor")
    bankAccount2 = BankAccount_INT("marcin")
    bankAccount3 = BankAccount_COVID19_firma("adam")
    bankAccount4 = BankAccount_INT("grzegorz")

    banks = [bankAccount1, bankAccount2, bankAccount3, bankAccount4]

    banksMap = mapBanksToKeyValue(banks)

    bankService = BankService(banksMap)

    accountNumber1 = bankAccount1.getAccountNumber()
    accountNumber2 = bankAccount2.getAccountNumber()
    accountNumber3 = bankAccount3.getAccountNumber()
    accountNumber4 = bankAccount4.getAccountNumber()

    bankService.deposit(accountNumber1, 200)
    bankService.deposit(accountNumber2, 210)
    bankService.deposit(accountNumber3, 220)
    bankService.deposit(accountNumber4, 230)
    bankService.print()

    listOfBanks = mapKeyValueToListOfBanks(bankService.getBanks())
    banksToCsv(listOfBanks)

    banksFromCsv = csvToBanks()
    banksMapFromCsv = mapBanksToKeyValue(banksFromCsv)
    bS = BankService(banksMapFromCsv)

    bS.print()


def mapBanksToKeyValue(banks):
    banksMap = {}
    for i in banks:
        banksMap.update({i.getAccountNumber(): i})
    return banksMap
    pass

def mapKeyValueToListOfBanks(banks):
    listBanks = []
    for bank in banks.values():
        listBanks.append(bank)

    return listBanks
    pass


def banksToCsv(banks):
    import csv
    with open("banks.csv", 'w') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(list(banks))
    pass


def csvToBanks():
    import csv

    banks = []
    with open('banks.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == "BankAccount_COVID19":
                bank = BankAccount_COVID19.instance(row[0], row[1], row[2], row[3])
                banks.append(bank)
            if row[2] == "BankAccount_COVID19_firma":
                bank = BankAccount_COVID19_firma.instance(row[0], row[1], row[2], row[3])
                banks.append(bank)
            if row[2] == "BankAccount_INT":
                bank = BankAccount_INT.instance(row[0], row[1], row[2], row[3])
                banks.append(bank)

    return banks
    pass

main()
