# Завдання 4
#
# Напишіть функцію, яка буде аналізувати текст, що надходить до неї,
# і виводити тільки унікальні слова на екран,
# загальну кількість слів і кількість унікальних слів.
import re


def print_text_info(text: str) -> None:
    pattern = r"(\w+\b)"
    pattern_unique = r"(\w+\b)(?!.*\1\b)"

    result = re.findall(pattern, text)
    result_unique = re.findall(pattern_unique, text)

    print("Unique words: ", result_unique)
    print("Total words count: ", len(result))
    print("Unique words count: ", len(result_unique))


if __name__ == "__main__":
    text = "glass shoes door window door glasses. window glasses"

    print_text_info(text)
