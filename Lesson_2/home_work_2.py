# Завдання 2
#
# Опишіть класи графічного об'єкта, прямокутника
# та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки.
# Створіть об'єкт кнопки та звичайного прямокутника.
# Викличте метод натискання на кнопку.
from turtle import Turtle
from typing import NamedTuple


class Point(NamedTuple):
    x: int | float
    y: int | float


class Rectangle:
    def __init__(self, top_left_point: 'Point', bottom_right_point: 'Point'):
        self._point_1 = top_left_point
        self._point_2 = bottom_right_point

    def draw(self):
        t = Turtle()

        t.teleport(*self._point_1)
        t.color('orange')  # Set pen color to red
        t.fillcolor('orange')  # Set fill color for shapes
        t.begin_fill()
        t.forward(self._point_2.x)  # Move forward X units
        t.left(90)  # Turn left by 90 degrees
        t.backward(self._point_2.y)  # Move backward Y units
        t.left(90)  # Turn left by 90 degrees
        t.forward(self._point_2.x)  # Move backward X units
        t.left(90)  # Turn left by 90 degrees
        t.backward(self._point_2.y)  # Move backward Y units
        t.end_fill()


class Button:
    def click(self, callback):
        if callable(callback):
            callback()


rect_1 = Rectangle(Point(50, 50), Point(140, 100))

button_1 = Button()
button_1.click(rect_1.draw)
