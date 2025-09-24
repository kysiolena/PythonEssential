# Завдання 3
#
# Створіть модуль для отримання простих чисел.
# Імпортуйте його з іншого модуля. Імпортуйте його окремі імена.

# 1. Імпортуйте його з іншого модуля.
import prime_numbers

# 2. Імпортуйте його окремі імена.
# from prime_numbers import prime_numbers_generator

if __name__ == '__main__':
    # 1
    print(list(prime_numbers.prime_numbers_generator(1, 100)))
    # 2
    # print(list(prime_numbers_generator(1, 100)))
