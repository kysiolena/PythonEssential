# Завдання 2
#
# Створити клас Contact з полями surname, name, age, mob_phone, email.
# Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job.
# Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів:
# __dict__, __base__, __bases__.
# Роздрукувати інформацію на екрані.

class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str):
        self._surname = surname
        self._name = name
        self._age = age
        self._mob_phone = mob_phone
        self._email = email

    def get_contact(self) -> None:
        print(self._surname, self._name, self._age, self._mob_phone, self._email)

    def sent_message(self) -> None:
        print(f'Message sent to {self._email} successfully!')


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str, job: str):
        super().__init__(surname, name, age, mob_phone, email)

        self._job = job

    def get_message(self) -> None:
        print(
            f'Hello, {self._name} {self._surname}! How are you? I\'m looking forward to talking about your job as {self._job}!')


contact_1 = Contact('Hello', 'World', 25, '+380991111111', 'mail@mail.com')
update_contact_1 = UpdateContact('UHello', 'UWorld', 52, '+380662222222', 'u-mail@mail.com', 'accountant')

if __name__ == '__main__':
    print('__BASE__')
    print(Contact.__base__)
    print(UpdateContact.__base__)
    print('*' * 20)

    print('__BASES__')
    print(Contact.__bases__)
    print(UpdateContact.__bases__)
    print('*' * 20)

    print('__DICT__')
    print(Contact.__dict__)
    print(UpdateContact.__dict__)
    print('*' * 20)

    update_contact_1.get_contact()
    update_contact_1.get_message()
    update_contact_1.sent_message()
