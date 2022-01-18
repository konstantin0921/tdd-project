import unittest
from money import Money
from portfolio import Portfolio

#       5 USD * 2 = 10 USD
#       10 EUR * 2 = 20 EUR
#       4002 KRW / 4 = 1000.5 KRW
#       5 USD + 10 USD = 15 USD
#       Remove redudant Money multipication tests

#       5 USD + 10 EUR = 17 USD    because 1 EUR = 1.2 USD
#       1 USD + 1100 KRW = 2200 KRW because 1 USD = 1100 KRW
#       Determine exchange rate based on the currencies involved(from to)
# Allow exchange rates to be modified
#       improve error handling when exchange rate is not defined


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

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

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        pf = Portfolio()
        pf.add(fiveDollars, tenEuros)
        expected = Money(17, "USD")
        actual = pf.evaluate("USD")
        self.assertEqual(expected, actual, "%s != %s" % (expected, actual))

    def testAdditionOfDollarsAndWon(self):
        oneDollar = Money(1, "USD")
        koreanWons = Money(1100, "KRW")
        pf = Portfolio()
        pf.add(oneDollar, koreanWons)
        expected = Money(2200, "KRW")
        actual = pf.evaluate("KRW")
        self.assertEqual(expected, actual, "%s != %s" % (expected, actual))

    def testAdditionWithMultipleMissingExchangeRates(self):
        oneDollar = Money(1, "USD")
        oneEuro = Money(1, "EUR")
        oneWon = Money(1, "KRW")
        pf = Portfolio()
        pf.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
            Exception,
            r"Missing exchange rate\(s\):\[USD->kalganid,EUR->kalganid,KRW->kalganid\]",
        ):
            pf.evaluate("kalganid")


if __name__ == "__main__":
    unittest.main()