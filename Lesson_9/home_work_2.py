# Завдання 2
#
# Повторіть інформацію про розглянуті на уроці стандартні модулі.
# Ознайомтеся також із модулями calendar, heapq, bisect, array, enum.

import array
import bisect
import calendar
import enum
import heapq

if __name__ == '__main__':
    print(calendar.calendar(2025))
    print(heapq.nlargest(10, range(1, 100)))
    print(bisect.bisect_left(range(1, 100), 2))
    print(array.array('i', list(range(1, 100))))
    print(enum.CONTINUOUS)
