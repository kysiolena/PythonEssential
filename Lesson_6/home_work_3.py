# Завдання 3
#
# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

class Reverse:
    def __init__(self, data: list | str | tuple):
        # Init data
        self.data = data

    def __iter__(self):
        # Init index
        self.index = 0

        return self

    def __next__(self):
        # Raise error in the end
        if self.index == len(self.data):
            raise StopIteration

        # Get index
        index = -1 * (self.index + 1)

        # Get item
        result = self.data[index]

        # Increase index
        self.index += 1

        # Return item
        return result


if __name__ == '__main__':
    # Str
    print('Str')
    reverse_str = Reverse('Hello')

    for item in reverse_str:
        print(item)
    print('=' * 3)

    # List
    print('List')
    reverse_list = Reverse([5, 85, 9, 7, 11, 6])

    for item in reverse_list:
        print(item)
    print('=' * 3)

    # Tuple
    print('Tuple')
    reverse_tuple = Reverse((9, 7, 11))

    for item in reverse_tuple:
        print(item)
    print('=' * 3)
