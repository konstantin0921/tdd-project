import unittest


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


# 5 USD * 2 = 10 USD
# 10 EUR * 2 = 20 EUR
# 4002 KRW / 4 = 1000.5 KRW
# 5 USD + 10 EUR = 17 USD    because 1 EUR = 1.2 USD
# 1 USD + 1100 KRW = 2200 KRW because 1 USD = 1100 KRW


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)


if __name__ == "__main__":
    unittest.main()