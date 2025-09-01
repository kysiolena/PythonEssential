# Завдання 7
#
# Створіть ієрархію класів транспортних засобів.
# У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм.
# Створіть кілька екземплярів.
# Виведіть інформацію щодо кожного транспортного засобу.

class Vehicle:
    is_move = True

    def __init__(self, name: str = 'Some Vehicle'):
        self.name = name

    def info(self):
        return f'Hi! I\'m a vehicle! My name is {self.name}.'


class FuelVehicle(Vehicle):
    is_need_fuel = True


class NoFuelVehicle(Vehicle):
    is_need_fuel = False


class Car(FuelVehicle):
    is_drive = True

    def info(self):
        return f'Hi! I\'m a car! I can drive. My name is {self.name}.'


class Airplane(FuelVehicle):
    is_fly = True

    def info(self):
        return f'Hi! I\'m an airplane! I can fly. My name is {self.name}.'


class Bicycle(NoFuelVehicle):
    is_drive = True

    def info(self):
        return f'Hi! I\'m a bicycle! I can drive and I don\'t need a fuel. My name is {self.name}.'


car_1 = Car('Honda')
airplane_1 = Airplane('Airbus')
bicycle_1 = Bicycle('Kross')

print(car_1.info())
print(airplane_1.info())
print(bicycle_1.info())
