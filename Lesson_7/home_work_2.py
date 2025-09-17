# Завдання 2
#
# Виведіть із списку чисел список квадратів парних чисел.
# Використовуйте 2 варіанти рішення: генератор та цикл

from typing import Generator


def two_pow_of_even_numbers_generator(numbers: list[int]) -> Generator[int]:
    for number in numbers:
        if number % 2 == 0:
            yield number ** 2


if __name__ == '__main__':
    # Numbers
    number_list = list(range(1, 50))

    # 1. Generator
    even_numbers_in_two_power_gen = list(two_pow_of_even_numbers_generator(number_list))

    # 2. Loop
    even_numbers_in_two_power = []
    for num in number_list:
        if num % 2 == 0:
            even_numbers_in_two_power.append(num ** 2)

    # 3. List Comprehension
    even_numbers_in_two_power_list_comprehension = [n ** 2 for n in number_list if n % 2 == 0]

    # Display results
    print(even_numbers_in_two_power_gen)
    print(even_numbers_in_two_power)
    print(even_numbers_in_two_power_list_comprehension)
