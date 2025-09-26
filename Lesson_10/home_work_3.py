# Завдання 3
#
# Користувач вводить з клавіатури пропозицію.
# Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.

import re


def get_last_three_symbols(text: str) -> str:
    pattern = r"(.{3})\s|\n"
    return re.findall(pattern, text)


if __name__ == "__main__":
    text = input("Enter your proposal: ")

    print(get_last_three_symbols(text + "\n"))
