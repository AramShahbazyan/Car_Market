# Seller-ը կունենա car_park, money, sold_cars ատրիբուտները։ car_park-ում լինելու են այն
# մեքենաները որոնք Seller֊ը պետք է վաճառի, այդ ցուցակը վերցվելու CarMarket֊ի get_seller_available_cars֊ից։
# Seller class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1․  sell - վաճառելու է մեքենան: Լինելու է public method
# 2. change_money - ավելացնելու/պակասացնելու է գումարը։ Լինելու է private method
# 3. return_car - ընդունելու է վերադարձի մեքենան։ Այստեղ պետք է նվազի վաճառողի գումարը, ավլանա գնորդի
# գումարը, CarMarket֊ում փոխվի մեքենայի ստատւսը (պետք է գրվի վերադառձի մասին ինֆօ)։ Լինելու է public method
# 4. get_available_cars - CarMarket֊ից (get_seller_available_cars) կվերցի կոնկրետ Seller֊ի հասանելի
# մեքենաների ցուցակը։ Լինելու է protected method
# 5. check_discount - կստուգի արդյոք գնորդի մեքենայի համար կա զեղչ, թե ոչ։ Լինելու է protected method
# 6. add_sold_car - կավեալցնի վաճառված մեքենան Seller֊ի sold_cars֊ում։ Պետք է նշվի մեքենայի մոդելը,
# գնորդի անուն/ազգանուն/քաղաք, գործարքի ամիս ամսաթիվը  հետևյալ ֆորմատով՝ "տարի-ամիս֊օր"

from datetime import datetime
from car import Car
from person import Person


class Seller(Person):
    def __init__(self, first_name, last_name, car_park, city, money=50000):
        super().__init__(first_name, last_name, city)
        self.money = money
        self.car_park = car_park
        self.sold_cars = {}

    def sell(self, car: Car):
        for i in self.car_park:
            if self.car_park[i] == car:
                self.car_park.pop(i)
                money = car.price - car.discount
                self.change_money(money)
                break
        else:
            print('not available car ')

    def change_money(self, money, car_sell=True):
        if car_sell:
            self.money += money
        else:
            self.money -= money
