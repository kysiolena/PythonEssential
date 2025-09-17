# Завдання 1
#
# Напишіть генератор, який повертає елементи заданого списку
# у зворотному порядку (аналог reversed).

from typing import Generator, Any


def reversed_generator(data: list) -> Generator[Any, Any, None]:
    for index, _ in enumerate(data):
        i = -1 * (index + 1)
        yield data[i]


if __name__ == '__main__':
    data_list = [56, 11, 99, 2, 6, 78, 43, 15]

    for number in reversed_generator(data_list):
        print(number)
