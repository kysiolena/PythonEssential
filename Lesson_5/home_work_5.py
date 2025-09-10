# Завдання 5
#
# Використовуючи код завдання 2 надрукуйте у терміналі інформацію,
# яка міститься у класах Contact та UpdateContact та їх екземплярах.
# Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів.
# Порівняйте їх. Зробіть відповідні висновки.


from Lesson_5.home_work_2 import Contact, UpdateContact, contact_1, update_contact_1

if __name__ == '__main__':
    print(Contact.__dict__)
    print(UpdateContact.__dict__)

    print('*' * 20)

    print(contact_1.__dict__)
    print(update_contact_1.__dict__)

    print('*' * 20)

    # Delete _job
    print('Delete _job: ', delattr(update_contact_1, '_job'))

    print('*' * 20)

    print(Contact.__dict__)
    print(UpdateContact.__dict__)

    print('*' * 20)

    print(contact_1.__dict__)
    print(update_contact_1.__dict__)

    print('*' * 20)
