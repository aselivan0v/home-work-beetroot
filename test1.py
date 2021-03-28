from random import randint
class Car():

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year if type(year) is int and year > 1900 else randint(1900, 2020)
        self.color = color
        self.total_km = 0
        self.speed = 0

    def repaint(self, new_color):
        self.color = new_color
        return f'New color for {self.model} is {self.color}'

    def drive(self, speed, time):
        self.speed = speed
        self.total_km += speed * time
        return f'Now speed is {self.speed}. Total {self.total_km} km driven'

    def __repr__(self):
        return f'Brand - {self.brand}, model - {self.model}'

    def __str__(self):
        return f'{self.brand}, {self.model}, {self.total_km}'

car_1 = Car('BMW', 'X5', 2010, 'Black')
car_2 = Car('VW', 'Polo', 2002, 'Red')

class Truck(Car):

    def __init__(self, brand, model, year, color, trailer = 0):
        super().__init__(brand, model, year, color)
        self.trailers = trailer

    def __str__(self):
        return f'Truck model - {self.model}'

    def attrach_trailer(self, trailer = 1):
        self.trailers += trailer

car_3 = Truck('Volvo', 'X10', 2019, 'Silver')

print(car_2)
print(car_3)