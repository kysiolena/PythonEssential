# Завдання 5
#
# З клавіатури вводиться рядок, в якому є інформація про прізвище,
# ім'я, дату народження, електронну адресу та відгук про курси учня.
# Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.

import re


def get_dict(text: str) -> str:
    pattern_name = r"([A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+\b)"
    pattern_birthday = r"\d{2}.\d{2}.\d{4}"
    pattern_emails = r"[A-Za-z-_.\d]{1,}@\w+\.\w{2,}"
    pattern_review = r"@.+\.\s(.+)"

    return {
        "name": re.findall(pattern_name, text)[0],
        "birthday": re.findall(pattern_birthday, text)[0],
        "email": re.findall(pattern_emails, text)[0],
        "review": re.findall(pattern_review, text)[0],
    }


if __name__ == "__main__":
    # Hello World. Birthday 07.07.1987. Email hello@world.com. Hfsd fd dg df gdfg dfg dfgfddf
    text_input = input("Enter your data: ")

    print(get_dict(text_input))
