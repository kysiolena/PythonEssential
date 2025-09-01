# Завдання 5
#
# Використовуючи код example_10, створіть статичний метод класу
# ( для створення використовуйте декоратор @staticmethod ),
# метод має приймати вік людини та перевіряти чи досягла вона повноліття (в Україні та Америці),
# метод має повертати True або False

from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, surname, name, birth_year):
        return cls(surname, name, date.today().year - birth_year)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


class MyClass3(MyClass1):
    @staticmethod
    def is_adult(age: int, is_usa: bool = False):
        if (is_usa and age < 21) or age < 18:
            return False

        return True


if __name__ == '__main__':
    m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
    m_per1.print_info()

    m_per2 = MyClass1.from_birth_year('Dovzhenko', 'Bogdan', 2000)
    m_per2.print_info()

    m_per3 = MyClass2.from_birth_year('Sydorchuk', 'Petro', 2010)
    print('isinstance(m_per3, MyClass2)', isinstance(m_per3, MyClass2))

    m_per4 = MyClass2.from_birth_year('Makuschenko', 'Dmytro', 2001)
    print('isinstance(m_per4, MyClass1)', isinstance(m_per4, MyClass1))

    print('issubclass(MyClass1, MyClass2)', issubclass(MyClass1, MyClass2))
    print('issubclass(MyClass2, MyClass1)', issubclass(MyClass2, MyClass1))

    print()
    print('Check your age')
    print()
    while True:
        age_person = int(input('Enter your age: '))
        is_usa_person = input('Do you live in USA? (Yes/No):')

        print(
            f'I\'m {age_person} years old. And I\'m {'adult' if MyClass3.is_adult(age_person, is_usa_person and is_usa_person.lower() == 'yes') else 'not adult yet'}!')
        print()

        is_end = input('Do you want to end the program? (Yes/No) ')

        if is_end and is_end.lower() == 'yes':
            break
