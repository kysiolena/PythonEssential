# Завдання 3
#
# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

from colorama import Fore

from Lesson_5.home_work_2 import contact_1, update_contact_1

if __name__ == '__main__':
    ATTRS = ['_surname', '_name', '_age', '_mob_phone', '_email', '_job']


    def get_attr(attr_item):
        print(Fore.GREEN + f'getattr({attr_item})' + Fore.RESET)
        try:
            print('contact_1 = ', getattr(contact_1, attr_item))
        except AttributeError as e:
            print(Fore.RED + f'Error: {e}' + Fore.RESET)

        try:
            print('update_contact_1 = ', getattr(update_contact_1, attr_item))
        except AttributeError as e:
            print(Fore.RED + f'Error: {e}' + Fore.RESET)

        print('*' * 20)


    def del_attr(attr_item):
        print(Fore.GREEN + f'delattr({attr_item})' + Fore.RESET)
        try:
            print('contact_1 = ', delattr(contact_1, attr_item))
        except AttributeError as e:
            print(Fore.RED + f'Error: {e}' + Fore.RESET)

        try:
            print('update_contact_1 = ', delattr(update_contact_1, attr_item))
        except AttributeError as e:
            print(Fore.RED + f'Error: {e}' + Fore.RESET)

        print('*' * 20)


    def has_attr(attr_item):
        print(Fore.GREEN + f'hasattr({attr_item})' + Fore.RESET)
        print('contact_1 = ', hasattr(contact_1, attr_item))
        print('update_contact_1 = ', hasattr(update_contact_1, attr_item))


    for attr in ATTRS:
        print()
        print('=' * 30)
        print()

        # Check attr
        has_attr(attr)

        # Show default
        get_attr(attr)

        # Delete
        del_attr(attr)

        # Check after Delete
        has_attr(attr)

        # Update
        print(Fore.GREEN + f'setattr({attr})' + Fore.RESET)
        print('contact_1 = ', setattr(contact_1, attr, 'Nice' + attr))
        print('update_contact_1 = ', setattr(update_contact_1, attr, 'UNice' + attr))
        print('*' * 20)

        # Show result of Update
        get_attr(attr)
