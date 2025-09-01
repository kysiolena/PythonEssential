# Завдання 1
#
# Створіть клас, який описує книгу.
# Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок.
# Визначте для нього методи _repr_ та _str_.

class Book:
    def __init__(self, author: str, name: str, year_of_publication: int, genre: str, reviews: list['Review']):
        self.author = author
        self._name = name
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.reviews = reviews

    def __repr__(self):
        return f'__repr__() Book(author={self.author}, name={self._name}, year_of_publication={self.year_of_publication}, genre={self.genre}, reviews={self.reviews})'

    def __str__(self):
        return f'__str__() Book(author={self.author}, name={self._name}, year_of_publication={self.year_of_publication}, genre={self.genre}, reviews={self.show_reviews()})'

    def show_reviews(self):
        return list(map(lambda r: str(r), self.reviews))

# Завдання 2
#
# Створіть клас, який описує відгук до книги.
# Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Review:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return f'{self.text}'

review_1 = Review('Good book!')
review_2 = Review('Very interesting book! I strongly recommend it.')
review_3 = Review('I\'s my favorite book.')

# print(repr(review_1))

book_1 = Book('Richard Bach', 'Jonathan Livingston Seagull', 1970, 'Story, Fiction, Parable, Self-development literature', [review_1, review_2, review_3])
book_2 = Book('Elizabeth Gilbert', 'Eat Pray Love', 2006, 'Memoirs, Biography, Autobiography, Travel Literature', [])

# Print __repr__ Book
# print(repr(book_1))
# print(repr(book_2))

# Print __str__ Book
# print(book_1)
# print(book_2)

# Завдання 4
#
# Створіть клас, який описує автомобіль.
# Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу,
# і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, model: str):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if not len(value):
            raise ValueError("Model cannot be empty string.")

        self.__model = value

    @model.deleter
    def model(self):
        del self.__model

class CarShowroom:
    def __init__(self, name: str, cars: list['Car']):
        self._name = name
        self.cars = cars

    def info(self):
        return f'There are {self.get_cars_count()} cars in car showroom «{self._name}»: {self.get_cars_list()}'

    def sell(self, car: 'Car'):
        car_index = self.cars.index(car)

        del self.cars[car_index]

    def sell_with_details(self, car: 'Car'):
        print(self.info())

        self.sell(car)

        print(f'The car «{car.model}» was sold from «{self._name}»')

        print(self.info())

    def get_cars_list(self):
        return list(map(lambda c: c.model, self.cars))

    def get_cars_count(self):
        return len(self.cars)

car_1 = Car('Cadillac CT4-V Blackwing')
car_2 = Car('Lucid Air')
car_3 = Car('Chevrolet Corvette')
car_4 = Car('Honda Accord')
car_5 = Car('Mercedes-Benz E450')

# print(car_4.model)
#
# car_4.model = 'Hello Test'
#
# print(car_4.model)
#
# del car_4.model
#
# print(car_4.model)


car_showroom_1 = CarShowroom('First', [car_1, car_3, car_5])
car_showroom_2 = CarShowroom('Second', [car_2, car_4, car_1, car_3, car_5])

car_showroom_1.sell_with_details(car_3)
car_showroom_2.sell_with_details(car_5)




