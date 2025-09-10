# Завдання 3
#
# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції,
# як властивості. Ознайомтеся з декоратором property у Python.
# Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру
# за шкалою Цельсія та Фаренгейта,
# причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class Temperature:
    def __init__(self, degrees: float | int, is_fahrenheit: bool = False):
        self._degrees = degrees
        self._is_fahrenheit = is_fahrenheit

    def __celsius_to_fahrenheit(self) -> float | int:
        return (self._degrees * 9 / 5) + 32

    def __fahrenheit_to_celsius(self) -> float | int:
        return (self._degrees * 5 / 9) - 32

    @property
    def degrees(self) -> float | int:
        return self._degrees

    @degrees.setter
    def degrees(self, value: float | int) -> None:
        self._degrees = value

    @property
    def is_fahrenheit(self) -> float | int:
        return self._is_fahrenheit

    @is_fahrenheit.setter
    def is_fahrenheit(self, value: float | int) -> None:
        self._is_fahrenheit = value

    def get_degrees(self, is_fahrenheit: bool = False) -> float | int:

        if is_fahrenheit:
            if self._is_fahrenheit:
                return self._degrees
            else:
                return self.__celsius_to_fahrenheit()
        else:
            if self._is_fahrenheit:
                return self.__fahrenheit_to_celsius()
            else:
                return self._degrees


# Using
if __name__ == '__main__':
    temperature_1 = Temperature(90)
    temperature_2 = Temperature(90, True)

    print('Default values of Temperatures')
    print('_')
    print(
        f'Temperature 1: {temperature_1.degrees} ({'Fahrenheit' if temperature_1.is_fahrenheit else 'Celsius'})')
    print(
        f'Temperature 2: {temperature_1.degrees} ({'Fahrenheit' if temperature_2.is_fahrenheit else 'Celsius'})')

    # Separator
    print('=' * 100)

    # Update degrees
    temperature_1.degrees = 126
    temperature_2.degrees = 11

    print('Updated values of Temperatures')
    print('_')
    print(
        f'Temperature 1: {temperature_1.degrees} ({'Fahrenheit' if temperature_1.is_fahrenheit else 'Celsius'})')
    print(
        f'Temperature 2: {temperature_2.degrees} ({'Fahrenheit' if temperature_2.is_fahrenheit else 'Celsius'})')

    # Separator
    print('=' * 100)

    # Update is_fahrenheit
    temperature_1.is_fahrenheit = True
    temperature_2.is_fahrenheit = False

    print('Updated is_fahrenheit of Temperatures')
    print('_')
    print(
        f'Temperature 1: {temperature_1.degrees} ({'Fahrenheit' if temperature_1.is_fahrenheit else 'Celsius'})')
    print(
        f'Temperature 2: {temperature_2.degrees} ({'Fahrenheit' if temperature_2.is_fahrenheit else 'Celsius'})')

    # Separator
    print('=' * 100)

    print('Get Temperature by get_degrees() method')
    print('_')
    print(
        f'Temperature 1 in Fahrenheit is {temperature_1.get_degrees(True)}')
    print(
        f'Temperature 1 in Celsius is {temperature_1.get_degrees()}')
    print(
        f'Temperature 2 in Fahrenheit is {temperature_2.get_degrees(True)}')
    print(
        f'Temperature 2 in Celsius is {temperature_2.get_degrees()}')
