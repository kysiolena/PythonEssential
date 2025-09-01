# Завдання 1
#
# Створіть клас Editor, який містить методи view_document та edit_document.
# Нехай метод edit_document виводить на екран інформацію про те,
# що редагування документів недоступне для безкоштовної версії.
# Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний,
# створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.

# Classes
class Editor:
    def view_document(self):
        print('Перегляд документів доступний')

    def edit_document(self):
        print('Редагування документів недоступне для безкоштовної версії')

class ProEditor(Editor):
    def edit_document(self):
        print('Редагування документів доступне')

# Interface
LICENSE_KEYS = ['first-key', 'second-key', 'third-key']

while True:
    user = None

    license_key = input('Enter your license key: ')

    if license_key and license_key.lower() in LICENSE_KEYS:
        user = ProEditor()
    else:
        user = Editor()

    user.view_document()
    user.edit_document()

    is_end = input('Do you want to end the program? (Yes/No) ')

    if is_end and is_end.lower() == 'yes':
        break





