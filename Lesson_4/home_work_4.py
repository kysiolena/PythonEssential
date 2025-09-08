# Завдання 4
#
# Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток,
# якщо користувач введе певне значення, і перехопіть цей виняток під час виклику функції.

from colorama import Fore


class WrongColorError(Exception):
    def __str__(self, *args, **kwargs) -> str:
        return 'Wrong color'


def show_color(color: str) -> None:
    COLORS = {'yellow': Fore.YELLOW, 'green': Fore.GREEN, 'blue': Fore.BLUE}

    try:
        if color.lower() not in COLORS.keys():
            raise WrongColorError

        print(COLORS[color] + f'{color.capitalize()} color')
        print(Fore.RESET)
    except WrongColorError as e:
        print(Fore.RED + f'Error: {color} is {e}')
        print(Fore.RESET)


# Using

if __name__ == '__main__':
    show_color('cyan')
    show_color('green')
    show_color('blue')
    show_color('red')
    show_color('yellow')
