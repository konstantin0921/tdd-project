from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, aMoney: Money, aCurrency: str) -> float:
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_usd

    def evaluate(self, currency: str):
        total = sum(self.__convert(i, currency) for i in self.moneys)
        return Money(total, currency)