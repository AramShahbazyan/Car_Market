class Person():
    def __init__(self, name, surname, city):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(city, str):
            self.name = name
            self.surname = surname
            self.city = city
        else:
            raise ValueError('Non correct value')


# p = Person('hakob', 'grigoryan', 'Yerevan')
# print(p.__dict__)