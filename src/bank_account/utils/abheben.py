from bank_account.bankaccount import BankAccount

def abheben(self, betrag: float[BankAccount]) -> None:
        if betrag > 0 :
            if self._kontostand >= betrag:
                self._kontostand -= betrag
                print(f"Es wurde '{betrag}' abgehoben")
                self._transaktionen.append(("Auszahlung", betrag))
            else:
                raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")

        else:
            raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")
