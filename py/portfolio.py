from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency: str):
        total = sum(i.amount for i in self.moneys)
        return Money(total, "USD")