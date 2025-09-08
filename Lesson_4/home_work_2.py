# Завдання 2
#
# Напишіть програму-калькулятор, яка підтримує такі операції:
# додавання, віднімання, множення, ділення та піднесення до ступеня.
# Програма має видавати повідомлення про помилку та продовжувати роботу
# під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.

from colorama import Fore


class Calculator:
    _num_1 = None
    _num_2 = None
    __available_operations = {
        'summing': '+',
        'subtracting': '-',
        'multiplying': '*',
        'dividing': '/',
        'powering': '^'
    }

    def __summing(self) -> int | float:
        return self._num_1 + self._num_2

    def __subtracting(self) -> int | float:
        return self._num_1 - self._num_2

    def __multiplying(self) -> int | float:
        return self._num_1 * self._num_2

    def __dividing(self) -> int | float:
        return self._num_1 / self._num_2

    def __powering(self) -> int | float:
        return self._num_1 ** self._num_2

    def _input_number(self) -> None:
        num = input(f'Enter the {'first' if self._num_1 is None else 'second'} number: ')

        self._save_number(num)

    def _save_number(self, num: str) -> None:
        try:
            num = float(num)

            if self._num_1 is None:
                self._num_1 = num
            else:
                self._num_2 = num

        except ValueError:
            print(Fore.RED + 'Invalid input')
            print(Fore.RESET)

    def _reset_numbers(self):
        self._num_1 = None
        self._num_2 = None

    def _calculate(self, operation: str) -> str:

        try:
            if operation not in self.__available_operations.values():
                raise ValueError('Invalid operation')

            result = None
            match operation:
                case '+':
                    result = self.__summing()
                case '-':
                    result = self.__subtracting()
                case '*':
                    result = self.__multiplying()
                case '/':
                    result = self.__dividing()
                case '^':
                    result = self.__powering()

            # Result
            result = Fore.GREEN + f'{self._num_1} {operation} {self._num_2} = {result}'

            self._reset_numbers()

            return result
        except ValueError as e:
            return Fore.RED + 'ValueError: ' + str(e)
        except ZeroDivisionError as e:
            return Fore.RED + 'ZeroDivisionError: ' + str(e)
        except Exception as e:
            return Fore.RED + 'Error: ' + str(e)

    def run(self):

        # Greeting message
        print('Let\'s calculate something!')

        while True:
            # Display options
            for op_name, op_key in self.__available_operations.items():
                print(f'{op_key} - {op_name.capitalize()}')

            # Set num_1 and num_2
            while self._num_1 is None or self._num_2 is None:
                self._input_number()

            # Set operation
            operation = input(
                f'What do you want to do with these numbers? ({', '.join(self.__available_operations.values())}) ')

            print(self._calculate(operation))

            # Reset style
            print(Fore.RESET, end='')

            is_end = input(f'Do you want to end the calculation? (y/n) ')
            if is_end.lower() == 'y':
                break
            else:
                self._reset_numbers()


# Using

if __name__ == '__main__':
    calculator_1 = Calculator()
    calculator_1.run()
