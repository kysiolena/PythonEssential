# Завдання 6
#
# Використовуючи код example_10, створіть класовий метод ( для створення використовуйте декоратор @classmethod ).
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття,
# для вирішення задачі використовуйте статичний метод створенний в завданні 5

from Lesson_2.home_work_5 import MyClass3

if __name__ == '__main__':
    class MyClass4(MyClass3):
        _instances = []

        def __init__(self, surname, name, age, is_usa: bool = False):
            super().__init__(surname, name, age)
            self.is_usa = is_usa
            MyClass4._instances.append(self)  # Add self to the list

        @classmethod
        def get_count_of_instances(cls):
            return len(cls._instances)

        @classmethod
        def get_count_of_adult_instances(cls):
            adult_instances = list(filter(lambda cl: cl.is_adult(cl.age), cls._instances))

            return len(adult_instances)


    person_1 = MyClass4('John', 'Doe', 45)
    person_2 = MyClass4('John', 'Doe', 15)
    person_3 = MyClass4('John', 'Doe', 20, True)
    person_4 = MyClass4('John', 'Doe', 90, True)
    person_5 = MyClass4('John', 'Doe', 20)
    person_6 = MyClass4('John', 'Doe', 14, True)
    person_7 = MyClass4('John', 'Doe', 18)

    print(
        f'Only {MyClass4.get_count_of_adult_instances()} instances are adult from {MyClass4.get_count_of_instances()} instances.')
