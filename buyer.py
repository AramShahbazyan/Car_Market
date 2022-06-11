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

from person import Person
import sqlite3


class Buyer(Person):
    def __init__(self, buy_money, name, surname, city):
        if isinstance(buy_money, int):
            super().__init__(name, surname, city)
            self.spent_money = 0
            self.buy_money = buy_money
            self.bought_cars = []
        else:
            raise ValueError('Non correct value')

    def buy(self, seller_name):
        if isinstance(seller_name, str):
            with sqlite3.connect("car.db") as db:
                curs = db.cursor()
                curs.execute("SELECT seller FROM cars_store")
                ls_seller = curs.fetchall()
                print(ls_seller)
                for sel in ls_seller:
                    print(sel)
                    if sel == seller_name:
                        self.bought_cars.append(curs.execute("SELECT seller FROM cars_store"))
                    else:
                        raise ValueError('This name seller not')

        else:
            raise ValueError('Non correct value')

    def return_car(self):
        pass

    def __change_money(self):
        pass

    def add_bought_cars(self, ):
        pass

    def print_my_cars(self):
        pass


b = Buyer(500000, 'dero', 'karapetyan', 'Yerevan')
print(b.bought_cars)
b.buy('dero')
print(b.bought_cars)