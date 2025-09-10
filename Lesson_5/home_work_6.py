# Завдання 6
#
# Використовуючи код завдання 2 надрукуйте у терміналі всі методи,
# які містяться у класі Contact та UpdateContact.

import inspect

from Lesson_5.home_work_2 import contact_1, update_contact_1

if __name__ == '__main__':
    print(inspect.getmembers(object=contact_1, predicate=inspect.ismethod))

    print('*' * 20)

    print(inspect.getmembers(object=update_contact_1, predicate=inspect.ismethod))
