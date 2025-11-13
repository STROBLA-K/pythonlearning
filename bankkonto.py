from typing import List, Tuple

class BankAccount:
    
    def __init__(self, inhaber: str, kontonummer: int, start_kontostand: float = 0.0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = start_kontostand
        self._transaktionen: List[Tuple[str, float]] = []

    def einzahlen(self, betrag: float) -> None:
        if betrag > 0 :
            self._kontostand += betrag
            print(f"Es wurde €'{betrag}' eingezahlt")
            self._transaktionen.append(("Einzahlung", betrag))
        else:
            print("Dieser Betrag kann nicht eingezahlt werden")
    
    def abheben(self, betrag: float) -> None:
        if betrag > 0 :
            if self._kontostand >= betrag:
                self._kontostand -= betrag
                print(f"Es wurde '{betrag}' abgehoben")
                self._transaktionen.append(("Auszahlung", betrag))
            else:
                raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")

        else:
            raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")

        
    def get_kontostand(self) -> float:
        return self._kontostand
    
    def get_transaktionen(self) -> list:
        return self._transaktionen
    
    def __str__(self):
        return f"Kunde: '{self.inhaber}'; Kontonummer: '{self.kontonummer}'; Kontostand: '{self._kontostand}'"
    
konto = BankAccount("A.S.", 1, 1000)
print(konto)

konto.einzahlen(50)
print(konto)

konto.abheben(100)

print("transaktionsverlauf:")
for transaktion in konto.get_transaktionen():
    print(f"{transaktion[0]}: {transaktion[1]}")


try:
    zahl = int(input("Geben sie eine Zahl zum abheben ein: " ))
    konto.abheben(zahl)
except ValueError as e:
    print(e)


class Jugendkonto(BankAccount):
    def abheben(self, betrag: float) -> None:
        if 0 < betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")
        

jugend_konto = Jugendkonto("maxi", 2, 5)
try:
    jugend_konto.abheben(50)
except ValueError as e:
    print(e)
    

print(jugend_konto.get_kontostand())