# Завдання 2
#
# Створіть 2 класи мови, наприклад, англійська та іспанська.
# В обох класів має бути метод greeting(). Обидва створюють різні привітання.
# Створіть два відповідні об'єкти з двох класів вище
# та викличте дії цих двох об'єктів в одній функції (функція hello_friend).

from abc import ABC, abstractmethod


class Language(ABC):
    @abstractmethod
    def greeting(self) -> str:
        pass


class English(Language):
    def greeting(self) -> str:
        return 'Hello!'


class Spanish(Language):
    def greeting(self) -> str:
        return 'Hola!'


class Ukrainian(Language):
    def greeting(self) -> str:
        return 'Вітаю!'


# Using
if __name__ == '__main__':
    def hello_friend() -> None:
        english_1 = English()
        spanish_1 = Spanish()
        ukrainian_1 = Ukrainian()

        print(f'Englishman say: "{english_1.greeting()}"')
        print(f'Hispanic say: "{spanish_1.greeting()}"')
        print(f'Ukrainian say: "{ukrainian_1.greeting()}"')


    hello_friend()
