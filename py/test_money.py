import unittest
import functools
import operator


class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency: str):
        total = sum(i.amount for i in self.moneys)
        return Money(total, "USD")


#       5 USD * 2 = 10 USD
#       10 EUR * 2 = 20 EUR
#       4002 KRW / 4 = 1000.5 KRW
# 5 USD + 10 USD = 15 USD
# 5 USD + 10 EUR = 17 USD    because 1 EUR = 1.2 USD
# 1 USD + 1100 KRW = 2200 KRW because 1 USD = 1100 KRW
# Remove redudant Money multipication tests


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuro(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(tenEuros.times(2), twentyEuros)

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(originalMoney.divide(4), expectedMoneyAfterDivision)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(portfolio.evaluate("USD"), fifteenDollars)


if __name__ == "__main__":
    unittest.main()