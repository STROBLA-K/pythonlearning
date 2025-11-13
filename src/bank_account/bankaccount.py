from typing import List, Tuple

class BankAccount:
    
    def __init__(self, inhaber: str, kontonummer: int, start_kontostand: float = 0.0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = start_kontostand
        self._transaktionen: List[Tuple[str, float]] = []

        
    def get_kontostand(self) -> float:
        return self._kontostand
    
    def get_transaktionen(self) -> list:
        return self._transaktionen
    
    def __str__(self):
        return f"Kunde: '{self.inhaber}'; Kontonummer: '{self.kontonummer}'; Kontostand: '{self._kontostand}'"
    
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
    
    def einzahlen(self, betrag: float) -> None:
        if betrag > 0 :
            self._kontostand += betrag
            print(f"Es wurde €'{betrag}' eingezahlt")
            self._transaktionen.append(("Einzahlung", betrag))
        else:
            print("Dieser Betrag kann nicht eingezahlt werden")
    