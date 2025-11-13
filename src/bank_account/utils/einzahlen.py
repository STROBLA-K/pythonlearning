from bank_account.bankaccount import BankAccount

def einzahlen(self, betrag: float[BankAccount]) -> None:
        if betrag > 0 :
            self._kontostand += betrag
            print(f"Es wurde €'{betrag}' eingezahlt")
            self._transaktionen.append(("Einzahlung", betrag))
        else:
            print("Dieser Betrag kann nicht eingezahlt werden")
    