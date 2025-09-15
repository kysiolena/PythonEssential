# Завдання 1
#
# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

if __name__ == '__main__':
    # 1
    # iterable = iter('Hello')
    #
    # print(next(iterable))
    # print(next(iterable))
    # print(next(iterable))
    # print(next(iterable))
    # print(next(iterable))
    # # Error StopIteration
    # print(next(iterable))

    # 2
    # отримання ітератора ітерабельного об’єкту
    iterable = iter('Hello')
    # нескінченний цикл
    while True:
        try:
            # отримання наступного елементу
            element = next(iterable)
            # якісь операції над елементом
            print(element)
        except StopIteration:
            # Якщо отримали StopIteration, выходимо з циклу
            break
