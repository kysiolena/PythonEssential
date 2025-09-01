# Завдання 3
#
# Створіть ієрархію класів із використанням множинного успадкування.
# Виведіть на екран порядок вирішення методів для кожного класу.
# Поясніть, чому лінеаризація даних класів виглядає саме так.

class Singer:
    can_sing = True

    @staticmethod
    def say():
        return 'I\'m the singer!'


class Swimmer:
    can_swim = True

    @staticmethod
    def say():
        return 'I\'m the swimmer!'


class Flyer:
    can_fly = True

    @staticmethod
    def say():
        return 'I\'m the flyer!'


class Bird:
    has_feathers = True
    has_beak = True

    @staticmethod
    def say():
        return 'I\'m the bird!'


class Duck(Bird, Swimmer, Flyer):
    pass


class Ostrich(Bird):
    pass


class Canary(Bird, Singer, Flyer):
    pass


class CodySimpson(Singer, Swimmer):
    pass


print(Duck.mro())
print(Duck.__mro__)
print(Duck.say())
print()

print(Ostrich.mro())
print(Ostrich.__mro__)
print(Ostrich.say())
print()

print(Canary.mro())
print(Canary.__mro__)
print(Canary.say())

print(CodySimpson.mro())
print(CodySimpson.__mro__)
print(CodySimpson.say())
