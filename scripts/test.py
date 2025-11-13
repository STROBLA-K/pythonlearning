from bank_account.bankaccount import BankAccount
from bank_account.jugendbankaccount import Jugendkonto
from bank_account.utils.einzahlen import einzahlen
from bank_account.utils.abheben import abheben


def main():
    konto = BankAccount("A.S.", 1, 1000)
    konto.einzahlen(50)
    konto.abheben(100)
    print(konto.get_kontostand())

if __name__ == "__main__":
    main()