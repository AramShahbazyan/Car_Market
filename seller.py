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


from person import Person


class Seller(Person):
    def __init__(self, sel_money, car_park, sold_cars, name, surname, city):
        if isinstance(sel_money, int):
            super().__init__(name, surname, city)
            self.sel_money = sel_money
            self.car_park = car_park
            self.sold_cars = sold_cars

    def sell(self):
        pass

    def __change_money(self):
        pass

    def return_car(self):
        pass

    def _get_available_cars(self):
        pass

    def _check_discount(self):
        pass

    def add_sold_car(self):
        pass


sel1 = Seller