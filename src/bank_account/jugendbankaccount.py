
from .bankaccount import BankAccount

class Jugendkonto(BankAccount):
    def abheben(self, betrag: float) -> None:
        if 0 < betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError(f"Der Betrag '{betrag}' kann nicht abgehoben werden")
        
