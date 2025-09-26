# Завдання 1
#
# Написати функцію, яка за допомогою регулярних виразів
# розбиває текст на окремі слова і знаходить частоту окремих слів.

import re

if __name__ == "__main__":
    text = (
        "The weather today is mild and pleasant, with temperatures hovering around 22°C. "
        "A gentle breeze is blowing from the west, carrying the scent of early autumn. "
        "The sky is partly cloudy, letting occasional rays of sunshine warm the day. "
        "There's no sign of rain, making it perfect for a walk or outdoor activities. "
        "Evening temperatures are expected to drop slightly, so a light jacket might be needed. "
        "Overall, a calm and comfortable day to enjoy."
    )

    pattern_words = r"([\w']+\b)"
    pattern_unique_words = r"([\w']+\b)(?!.*\1\b)"

    words = re.findall(pattern_words, text.lower())
    words_unique = re.findall(pattern_unique_words, text.lower())

    print("About the Whether story".upper())
    print("*" * 20)
    print(text)
    print("*" * 20)

    for word in words_unique:
        word_count = len(re.findall(rf"\b{word}\b", text.lower()))
        print(f"Count of «{word}» is {word_count}")
