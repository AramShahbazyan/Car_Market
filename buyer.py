# Buyer-ը կունենա money, spent_money և bought_cars ատրիբուտները։
# Buyer-ի money-ին կփոխանցեք կամայական արժեք` Buyer օբյեկտի ստեղծման պահին,
# իսկ spent_money-ը պետք է ունենա 0 սկզբնական արժեք (այս ատրիբուտը ցույց կտա գնորդի ծախսած գումարը)։

# Buyer class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1. buy - գնելու է վաճառողից մեքենա։ Լինելու է public method
# 2. return_carr - վերադարձնելու է մեքենան (դրանից բխող բոլոր update-ները պետք է կարատվեն)։ Լինելու է public method
# 3. change_money - ավելացնելու/պակասացնելու է գումարը։ Լինելու է private method
# 4. add_bought_cars - ավելացնելու է գնված մեքենան bought_cars֊ում։ Պետք է նշվի մեքենայի մոդելը,
# վաճառողի անուն/ազգանուն/քաղաք, գործարքի ամիս ամսաթիվը  հետևյալ ֆորմատով՝ "տարի-ամիս֊օր"
# 5. print_my_cars - ցույց կտա գնորգի գնված մեքենաները։ Լինելու է public method
from datetime import datetime

from carMarket import CarMarket
from person import Person

from car import Car
from seller import Seller


class Buyer(Person):

    def __init__(self, first_name, last_name, city, money=50000):
        super().__init__(first_name, last_name, city)
        self.money = money
        self.spent_money = 0
        self.bought_cars = {}

    def generate_key(self):
        key = 1
        while True:
            if key in list(self.bought_cars.keys()):
                key += 1
            else:
                return key

    def buy(self, car: Car, seller: Seller):
        self.add_bought_cars(car, seller)
        self.money -= car.price - car.discount
        self.spent_money += car.price - car.discount

    def return_car(self, car: Car):
        self.bought_cars.pop(car)
        self.money += car.price - car.discount

    def change_money(self, money):
        self.money += money

    def add_bought_cars(self, car, seller: Seller):
        key = self.generate_key()
        self.bought_cars[key] = {
            'car': car,
            'date': datetime.now().strftime("%d-%B-%Y"),
            'seller': {
                'name': seller.first_name,
                'lastname': seller.last_name,
                'city': seller.city
            }
        }

    def print_my_cars(self):
        for i in self.bought_cars:
            print(self.bought_cars[i]['car'])


if __name__ == '__main__':
    carpark = CarMarket.carpark
    seller_1 = Seller('aram', 'shahbazyan', 'yerevan', carpark)
    car_1 = Car('BMW', 5000, 1000)
    buyer_1 = Buyer('meliq', 'harutyunyan', 'yerevan')

    buyer_1.buy(car_1, seller_1)
    buyer_1.print_my_cars()
    print(buyer_1.bought_cars)
    # add_new_car = CarMarket()
    # add_new_car.add_car(car_1, seller_1)
    print(carpark)
