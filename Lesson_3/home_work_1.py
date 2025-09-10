# Завдання 1
#
# Створіть клас, який описує автомобіль.
# Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(
            self,
            model: str,
            year: int,
            mileage: int,
            color: str,
            fuel: str,
            engine_capacity: int,
            number_of_passengers: int
    ):
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self._color = color
        self._fuel = fuel
        self._engine_capacity = engine_capacity
        self._number_of_passengers = number_of_passengers

    def set_model(self, name: str):
        self.__model = name

    def get_model(self):
        return self.__model

    def set_year(self, year: int):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_mileage(self, mileage: int):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_color(self, color: str):
        self._color = color

    def get_color(self):
        return self._color

    def set_fuel(self, fuel: str):
        self._fuel = fuel

    def get_fuel(self):
        return self._fuel

    def set_engine_capacity(self, engine_capacity: int):
        self._engine_capacity = engine_capacity

    def get_engine_capacity(self):
        return self._engine_capacity

    def set_number_of_passengers(self, number_of_passengers: int):
        self._number_of_passengers = number_of_passengers

    def get_number_of_passengers(self):
        return self._number_of_passengers


if __name__ == '__main__':
    car_1 = Car(
        'Honda',
        19,
        100,
        'green',
        'electric',
        4,
        4
    )

    print(f'model = {car_1.get_model()}')
    print(f'year = {car_1.get_year()}')
    print(f'mileage = {car_1.get_mileage()}')
    print(f'color = {car_1.get_color()}')
    print(f'fuel = {car_1.get_fuel()}')
    print(f'engine_capacity = {car_1.get_engine_capacity()}')
    print(f'number_of_passengers = {car_1.get_number_of_passengers()}')
