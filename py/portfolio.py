from money import Money
from bank import Bank
from typing import Union


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank: Bank, currency: str) -> Union[Money, Exception]:
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)

        if not failures:
            return Money(total, currency)

        failureMsg = ",".join(f.args[0] for f in failures)
        raise Exception(f"Missing exchange rate(s):[{failureMsg}]")