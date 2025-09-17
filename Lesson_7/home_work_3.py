# Завдання 3
#
# Напишіть функцію-генератор для отримання n перших простих чисел.

from typing import Generator


def prime_numbers_generator(min_number: int, max_number: int) -> Generator[int, None, None]:
    for num in range(min_number, max_number + 1):
        if num > 1:
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False

                    break

            if is_prime:
                yield num


if __name__ == '__main__':
    print(list(prime_numbers_generator(1, 100)))
