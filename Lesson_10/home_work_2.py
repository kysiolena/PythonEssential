# Завдання 2
#
# Написати функцію, яка за допомогою регулярних виразів з файлу
# витягує дані про дату народження, телефон та електронну адресу.
# Дані потрібно записати до іншого файлу.

import json
import re

if __name__ == "__main__":
    with open("user_data.txt", "r") as f:
        data = f.read()

    pattern_birthday = r"\d{2}.\d{2}.\d{4}"
    pattern_phone = r"\+38\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}"
    pattern_emails = r"[A-Za-z-_.\d]{1,}@\w+\.\w{2,}"

    birthdays = re.findall(pattern_birthday, data)
    phones = re.findall(pattern_phone, data)
    emails = re.findall(pattern_emails, data)

    print(birthdays, phones, emails)

    users_data = []
    for index, phone in enumerate(phones):
        users_data.append(
            {
                "phone": phone,
                "email": emails[index],
                "birthday": birthdays[index],
            }
        )

    with open("users_data.json", "w", encoding="utf-8") as f:
        json.dump(users_data, f, ensure_ascii=False, indent=2)
