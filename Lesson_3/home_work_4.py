# Завдання 4
#
# Опишіть два класи Base та його спадкоємця Child з методами method(),
# який виводить на консоль фрази відповідно "Hello from Base" та "Hello from Child",
# using classmethod (@classmethod) decorator.

class Base:
    @classmethod
    def method(cls):
        print('Hello from Base')


class Child(Base):
    @classmethod
    def method(cls):
        print('Hello from Child')


if __name__ == '__main__':
    Base.method()
    Child.method()
