class Person:
    def __init__(self, first_name, last_name, city):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(city, str):
            self.first_name = first_name
            self.last_name = last_name
            self.city = city

        else:
            raise ValueError('Non correct value')


# p = Person('hakob', 'grigoryan', 'Yerevan')
# print(p.__dict__)