from money import Money


class Bank:
    def __init__(self):
        self.exchangeRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        k = currencyFrom + "->" + currencyTo
        self.exchangeRates[k] = rate

    def convert(self, aMoney: Money, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney

        k = aMoney.currency + "->" + aCurrency
        if k in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[k], aCurrency)
        else:
            raise Exception(k)