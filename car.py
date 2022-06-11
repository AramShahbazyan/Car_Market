class Car():
    def __init__(self, seller_name, make, model, year, price):
        if isinstance(seller_name, str) and isinstance(make, str) and isinstance(model, str) \
                and isinstance(year, int) and isinstance(price, int):
            self.seller_name = seller_name
            self.make = make
            self.model = model
            self.year = year
            self.price = price
        else:
            raise ValueError('Non correct value')

