# Завдання 1
#
# Напишіть скрипт, який створює текстовий файл і записує до нього
# 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

import random


def create_file(count_of_numbers: int = 10000) -> None:
    file_name = f'numbers_{count_of_numbers}.txt'
    with open(file_name, 'w') as f:
        for i in range(count_of_numbers):
            if i % 3 == 0:
                number = random.randint(-1 * count_of_numbers, count_of_numbers)
            else:
                number = random.uniform(-1 * count_of_numbers, count_of_numbers)

            f.write(f'{number}\n')

    print(f'File {file_name} was created!')


def display_sum_numbers_from_file(file_name: str | None = None) -> None:
    if file_name is None:
        print(f'File name is required!')
    else:
        with open(file_name, 'r') as f:
            numbers = f.readlines()

        numbers = map(float, numbers)

        print(f'Sum of numbers from {file_name} is: {sum(numbers)}!')


if __name__ == '__main__':
    create_file()

    display_sum_numbers_from_file('numbers_10000.txt')
