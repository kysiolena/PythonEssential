# Створіть програму нотатки.
# У користувача є меню
# 1 - Додати нотатку
# 2 - Переглянути всі нотатки
# 0 - Вихід.
# Програма працює доки користувач її не завершить.
# Якщо користувач ввів 1 запитайте у нього текст нотатки та день тиждня
# коли це треба зробити отриману інформацію запишіть у текстовий файл.
# Коли користувач натискає 2 виведіть нотатки в форматі
# НОТАТКА - ДЕНЬ ТИЖДНЯ
# кожну нотатку з нового рядку.
# Коли користувач натискає 0 завертшіть програму


def notate():
    while True:
        choice = input(
            'MENU'
            '\n 1 - Додати нотатку'
            '\n 2 - Переглянути всі нотатки'
            '\n 0 - Вихід.'
            '\n Your choice is : '
        )

        match choice:
            case '1':
                # запитайте у нього текст нотатки та день тиждня коли це треба зробити
                note = input('Enter text for note: ')
                note_week_day = input('Enter week day: ')

                if '|' not in note and '|' not in note_week_day:
                    with open('notes.txt', 'a') as f:
                        f.write(f'{note}|{note_week_day}\n')
                else:
                    print('Note and week day can\'t be separated by |')

            case '2':
                # виведіть нотатки в форматі НОТАТКА - ДЕНЬ ТИЖДНЯ
                with open('notes.txt', 'r') as f:
                    notes = f.readlines()

                for note in notes:
                    note_list = note.split('|')

                    print(f'{note_list[0].strip()} - {note_list[1].strip()}')
            case '0':
                break


if __name__ == '__main__':
    notate()
