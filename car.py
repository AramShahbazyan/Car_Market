class Car:
    def __init__(self, model, price, discount):
        self.model = model

        self.price = price
        self.discount = discount

    def __repr__(self):
        return f'{self.model}-{self.price}- {self.discount} '
