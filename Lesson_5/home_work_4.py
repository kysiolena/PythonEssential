# Завдання 4
#
# Використовуючи код з завдання 2, створити 2 екземпляри обох класів.
# Використати функції
# isinstance() – для перевірки екземплярів класу (за яким класом створені)
# та issubclass() – для перевірки і визначення класу-нащадка.


from Lesson_5.home_work_2 import Contact, UpdateContact, contact_1, update_contact_1

if __name__ == '__main__':
    print('isinstance(contact_1, Contact) = ', isinstance(contact_1, Contact))
    print('isinstance(update_contact_1, Contact) = ', isinstance(update_contact_1, Contact))
    print('isinstance(contact_1, UpdateContact) = ', isinstance(contact_1, UpdateContact))
    print('isinstance(update_contact_1, UpdateContact) = ', isinstance(update_contact_1, UpdateContact))

    print('*' * 20)

    print('issubclass(UpdateContact, Contact) = ', issubclass(UpdateContact, Contact))
    print('issubclass(Contact, UpdateContact) = ', issubclass(Contact, UpdateContact))
