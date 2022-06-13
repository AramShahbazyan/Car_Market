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


class CarMarket:
    carpark = {}

    def generate_key(self, seller: Seller):
        key = 1
        while True:
            if key in list(CarMarket.carpark[seller].keys()):
                key += 1
            else:
                return key

    def add_car(self, car: Car, seller: Seller):
        key = self.generate_key(seller)
        CarMarket.carpark[seller.first_name][key] = {'model': car.model,
                                                     'price': car.price,
                                                     'discount': car.discount}

    # def set_discount(self, seller, index, dis):
    #     if CarMarket.carpark[seller] == seller:
    #         CarMarket.carpark[seller][index]['discount'] = dis

    # def get_sold_car_history(self):

    # def return_car(self, seller: Seller, car: Car):
    #     CarMarket.carpark
    #

    def get_seller_available_cars(self, seller: Seller):
        for i in CarMarket.carpark:
            if i == seller.first_name:
                return CarMarket.carpark[i]

    def get_car_available_discount(self, seller: Seller, key, car: Car):
        return CarMarket.carpark[seller.first_name][key][car.discount]

market1 = CarMarket()
carpark = CarMarket.carpark
car1 = Car('BMW', 14000, 500)
seller1 = Seller(first_name='eva', last_name='papoyan', car_park=carpark, city='yervan')
# market1.add_car(car1, seller1)
market1.add_car(car1, seller1)
# market1.set_discount()
