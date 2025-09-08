# Завдання 3
#
# Опишіть клас співробітника, який вміщує такі поля:
# ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані.
# Введіть список працівників із клавіатури.
# Виведіть усіх співробітників, які були прийняті після цього (введеного з клавіатури) року.

from datetime import date

from colorama import Fore

DEPARTMENTS = ('design', 'development', 'marketing')


class Employee:
    _first_name: str = None
    _last_name: str = None
    _department: str = None
    _start_work: int = None
    __employees: list['Employee'] = []

    def __init__(self, first_name, last_name, department, start_work):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_work = start_work

        self.__employees.append(self)

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value) -> None:
        if not value:
            raise ValueError('First name cannot be empty')

        value = str(value).strip()
        if not len(value) or len(value) < 3:
            raise ValueError('First name must be at least 3 characters')

        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value) -> None:
        if not value:
            raise ValueError('Last name cannot be empty')

        value = str(value).strip()
        if not len(value) or len(value) < 3:
            raise ValueError('Last name must be at least 3 characters')

        self._last_name = value

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value) -> None:
        if not value:
            raise ValueError('Department cannot be empty')

        value = str(value).strip().lower()
        if value not in DEPARTMENTS:
            raise ValueError(f'Department «{value}» not exist')

        self._department = value

    @property
    def start_work(self) -> int:
        return self._start_work

    @start_work.setter
    def start_work(self, value) -> None:
        if not value:
            raise ValueError('Year of start work cannot be None')

        current_year = date.today().year
        min_year = current_year - 200

        value = int(value)
        if value < min_year or (value > current_year):
            raise ValueError(f'Year of start work must be between {min_year} and {current_year}')

        self._start_work = value

    @staticmethod
    def _show_employee(employee_item: 'Employee') -> str:
        return f'{employee_item.first_name} {employee_item.last_name}, {employee_item.department}, {employee_item.start_work}'

    @classmethod
    def show_employees(cls, employees_list: list['Employee'] | None = None) -> list['str']:
        return list(map(lambda em: cls._show_employee(em), (employees_list or cls.__employees)))

    @classmethod
    def show_employees_that_employed_after_year(cls, year: int) -> list['str']:
        empls = [empl for empl in cls.__employees if empl.start_work >= year]

        return cls.show_employees(empls)


# Using

if __name__ == '__main__':
    while True:
        # Create Employee
        employee_data = input('Enter by comma Firstname, Lastname, Department and Start Work of Employee: ')

        try:
            employee_data = employee_data.split(',')
            employee = Employee(*employee_data)

            print(Fore.BLUE + f'Created Employee {employee.first_name} {employee.last_name}')
            print(Fore.RESET, end='')
        except Exception as e:
            print(Fore.RED + f'Error: {e}')
            print(Fore.RESET, end='')

        is_end = input('Do you want to end the program? (y/n) ')

        if is_end.lower() == 'y':
            break

    while True:
        print('All Employees: ')
        print(Employee.show_employees())

        print()

        start_year = int(input('After what year of employment do you want to show employees: '))

        print(Employee.show_employees_that_employed_after_year(start_year))

        is_end = input('Do you want to end the program? (y/n) ')

        if is_end.lower() == 'y':
            break
