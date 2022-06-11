# CarMarket class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1․  add_car - ավելացնում է նոր մեքենա մեքենաների ցուցակ։
# 2. remove_car - ջնջելու է մեքենա/մեքենաներ։ Լինելու է private method
# 3. set_discount - զեղչ է դնելու մեքենայի/մեքենաներ վրա։ Լինելու է protected method
# 4. get_sold_car_history- վերադարձնելու է կոնրետ վաճառողի վաճառած մեքենաները։
# Յուրաքանչյուր մեքենայի գինը, գործարքի օր/ամիս/ամսաթիվը, գնորդի անունը/ազգանուն/քաղաք,
# եթե մեքենան ունեցել է զեղչ, ապա նաև զեղչը, եթե մեքենայի վերադարձ է կարարվել,
# ապա նաև վերադարձի մասին ինֆոն։ Լինելու է private method
# 5. return_car - մեքենայի վերադարձ գնորդի կողմից, այս դեպքում վաճարքի պատմություն մեջ՝
# վերադարձրած մեքենայի համար գրվում է, որ այն վերադարձվել է և վերադարձի պատճառը։ Լինելու է private method
# 6. get_seller_available_cars - վերադարձնելու է Seller-ի մոտ ներկա պահին վաճառվող մեքենաները։
# Լինելու է protected method
# 7․ get_car_available_discount -  կվերադարձնի մեքենայի համար հասանելի զեղչը:

from car import Car
from seller import Seller
import sqlite3


class CarMarket(Car):
    def __init__(self, seller_name, make, model, year, price):
        super().__init__(seller_name, make, model, year, price)
        self.discount = 0

    def add_car(self):
        with sqlite3.connect("car.db") as db:
            curs = db.cursor()
            curs.execute("INSERT INTO cars_store VALUES (?, ?, ?, ?, ?, ?)",
                         (self.seller_name, self.make, self.model, self.year, self.price, self.discount))
        db.commit()

    def remove_car(self, name_seller):
        with sqlite3.connect("car.db") as db:
            curs = db.cursor()
            remove_sel_car = f"DELETE FROM cars_store WHERE seller = '{name_seller}'"
            curs.execute(remove_sel_car)

    def set_discount(self, car_make, dis):
        if isinstance(dis, int):
            with sqlite3.connect("car.db") as db:
                curs = db.cursor()
                curs.execute("SELECT make FROM cars_store")
                for i in curs.fetchall():
                    if i[0] == car_make:
                        discount_update = f"UPDATE  cars_store SET discount = '{dis}' WHERE make = '{car_make}'"
                        curs.execute(discount_update)

    def __get_sold_car_history(self):
        pass

    def __return_car(self):
        pass

    def get_seller_available_cars(self, seller_name):
        with sqlite3.connect("car.db") as db:
            curs = db.cursor()
            seller_cars = f"SELECT * FROM cars_store WHERE seller = '{seller_name}'"
            curs.execute(seller_cars)
            for i in curs.fetchall():
                print(i)

    def get_car_available_discount(self):
        pass


c = CarMarket('samo', 'AUDI', 'A8', 2021, 160000)
c1 = CarMarket('dero', 'BMW', 'X5', 2020, 60000)
c2 = CarMarket('vaxo', 'Mercrdrs', 'cls 550', 2022, 200000)
c3 = CarMarket('makich', 'mazda', 'cx 5', 2019, 50000)
# c.add_car()
# c1.add_car()
# c2.add_car()
# c3.add_car()
# c.remove_car('samo')
# c.set_discount('BMW', 5)
c.get_seller_available_cars('vaxo')
