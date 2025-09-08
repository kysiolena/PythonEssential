# Завдання 5
#
# Створіть програму спортивного комплексу, у якій передбачене меню:
# 1 - перелік видів спорту,
# 2 - команда тренерів,
# 3 - розклад тренувань,
# 4 - вартість тренувань.
# Дані зберігати у словниках. (не зрозуміла, що тут в словниках треба було зберігати. Зробила класи та списки)
# Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню.
# Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
import random


class TrainerError(Exception):
    def __str__(self):
        return 'Тренера не знайдено'


class Training:
    kind_of_sport: str = None
    trainer: str = None
    day_of_week: str = None
    time: str = None
    cost: float = None

    def __init__(self, kind_of_sport, trainer, day_of_week, time, cost):
        self.kind_of_sport = kind_of_sport
        self.trainer = trainer
        self.day_of_week = day_of_week
        self.time = time
        self.cost = cost


class SportsComplex:
    _kinds_of_sports: list[str] = []
    _trainers: list[str] = []
    _trainings: list['Training'] = []

    def __init__(self, name: str):
        self.__name = name

    def add_kind_of_sport(self, sport_name: str):
        self._kinds_of_sports.append(sport_name)

    def add_trainer(self, trainer_name: str):
        self._trainers.append(trainer_name)

    def add_training(self, tr: 'Training'):
        self._trainings.append(tr)

    def get_kinds_of_sports(self) -> list[str]:
        return self._kinds_of_sports

    def get_trainers(self) -> list[str]:
        return self._trainers

    def get_trainings(self, trainings: list['Training'] | None = None) -> list[str]:
        return list(
            map(lambda t: f'{t.kind_of_sport} | {t.day_of_week}, {t.time} - {t.trainer} [{t.cost}]',
                (trainings or self._trainings)))

    def get_trainings_by_trainer_name(self, trainer: str) -> list[str]:
        if trainer not in self._trainings:
            raise TrainerError

        trainings = [t for t in self._trainings if t.trainer.lower() == trainer.lower()]

        return self.get_trainings(trainings)

    def get_costs(self) -> list[float]:
        costs = list(
            map(lambda t: t.cost, self._trainings))

        costs.sort()

        return costs


# Using

if __name__ == '__main__':
    # Init
    KIND_OF_SPORTS = ['swimming', 'karate', 'chess']
    TRAINERS = ['A', 'B', 'C', 'D', 'E', 'F']
    DAY_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    TIMES = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']

    sports_complex = SportsComplex('SportLife')

    for kind_of_sport_item in KIND_OF_SPORTS:
        sports_complex.add_kind_of_sport(kind_of_sport_item)

    for trainer_item in TRAINERS:
        sports_complex.add_trainer(trainer_item)

    for _ in range(1, 50):
        training_item = Training(
            random.choice(KIND_OF_SPORTS),
            random.choice(TRAINERS),
            random.choice(DAY_OF_WEEK),
            random.choice(TIMES),
            random.randint(100, 800)
        )
        sports_complex.add_training(training_item)

    while True:
        print('МЕНЮ')
        print('\t 1 - перелік видів спорту,')
        print('\t 2 - команда тренерів,')
        print('\t 3 - розклад тренувань,')
        print('\t 4 - вартість тренувань,')
        print('\t 5 - список тренувань за прізвищем тренера.')

        choice = int(input('Зробіть свій вибір: '))
        if choice == 1:
            print(sports_complex.get_kinds_of_sports())
        elif choice == 2:
            print(sports_complex.get_trainers())
        elif choice == 3:
            print(sports_complex.get_trainings())
        elif choice == 4:
            print(sports_complex.get_costs())
        elif choice == 5:
            trainer_name = input('Введіть ім\'я тренера: ')

            try:
                print(sports_complex.get_trainings_by_trainer_name(trainer_name))
            except TrainerError as e:
                print(f'Error: {e}')
        else:
            print('Wrong choice')

        is_end = input('Do you want to end the program? (y/n) ')

        if is_end.lower() == 'y':
            break
