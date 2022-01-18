from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, aMoney: Money, aCurrency: str) -> float:

        exchangeRates = {
            "EUR->USD": 1.2,
            "USD->KRW": 1100,
        }

        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            k = aMoney.currency + "->" + aCurrency
            return aMoney.amount * exchangeRates[k]

    def evaluate(self, currency: str):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if not failures:
            return Money(total, currency)

        failureMsg = ",".join(f.args[0] for f in failures)
        raise Exception(f"Missing exchange rate(s):[{failureMsg}]")