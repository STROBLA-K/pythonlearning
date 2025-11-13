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
    