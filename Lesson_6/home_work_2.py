# Завдання 2
#
# Взявши за основу код прикладу example_5.py,
# розширте функціональність класу MyList, додавши методи:
# + очищення списку,
# - додавання елемента у довільне місце списку,
# + видалення елемента з кінця та довільного місця списку.

class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def insert(self, index: int | None, element):
        if index < 0:
            index = 0
        elif index is None or (len(self) and index >= len(self)):
            index = len(self)

        # Якщо список порожній або індекс дорівнює останньому
        if len(self) == 0 or index == len(self):
            self.append(element)

        else:
            # Создание элемента списка
            node = MyList._ListNode(element)

            # Наступний елемент
            node_next = self._head
            for _ in range(index):
                node_next = node_next.next

            # Зміна будь-якого індексу окрім 0
            if index > 0:
                node.prev = node_next.prev
                node.next = node_next
                node_next.prev = node

                if node.prev:
                    node.prev.next = node

                if index == 1:
                    self._head.next = node

            else:
                node_next.prev = node
                node.next = node_next
                self._head = node

            # Збільшення довжини списку
            self._length += 1

    def clear(self):
        """Очищення списку"""
        self._head = self._tail = None

        self._length = 0

    def pop(self, index: int | None = None):
        """Видалення елементу списку"""

        del self[index]

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __delitem__(self, index: int | None = None):
        if index is not None and not 0 <= index < len(self):
            raise IndexError('Index out of range')

        # Якщо тільки один елемент був
        if self._head is self._tail:
            self.clear()

        # Якщо індекс не заданий або дорівнює останньому
        if self._tail is not None and (index is None or index == len(self) - 1):
            node_new_last = self._head
            for i in range(len(self) - 1):
                if node_new_last.next is self._tail:
                    break

                node_new_last = node_new_last.next

            node_new_last.next = None

            self._tail = node_new_last

        elif self._tail is not None and index is not None:
            # Елемент для видалення
            node_for_delete = self._head
            for _ in range(index):
                node_for_delete = node_for_delete.next

            # Попередній елемент
            node_prev = self._head
            for i in range(index):
                if node_prev.next is node_for_delete:
                    break

                node_prev = node_prev.next

            # Наступний елемент
            node_next = self._head
            for i in range(index + 1):
                node_next = node_next.next

            # Видалення будь-якого індексу окрім 0
            if index > 0:
                node_prev.next = node_for_delete.next
                node_next.prev = node_for_delete.prev
            else:
                node_next.prev = None
                self._head = node_next
        # Зменшення довжини списку
        self._length -= 1

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([3, 9, 1, 11])

    # Display item by index
    # print('Display item by index: ', my_list[2])

    # Display items
    print('Display items: ', my_list.__dict__)

    # Вывод самого списка
    print(my_list)

    # Вывод длины списка
    print('List length: ', len(my_list))

    # Delete
    my_list.pop(0)

    # Delete
    del my_list[1]

    # Вывод длины списка
    print('List length after delete: ', len(my_list))

    # Display items
    print('Display items: ', my_list.__dict__)

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    my_list.clear()
    print('Cleared list')

    my_list.insert(-99, 88)
    my_list.insert(500, 77)
    my_list.insert(1, 22)
    my_list.insert(0, 4)
    my_list.insert(2, 12)

    # Повторный обход списка
    for element in my_list:
        print(element)


if __name__ == '__main__':
    main()
