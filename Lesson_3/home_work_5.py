# Завдання 5
#
# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape.
# Перевизначте їх методи. Створіть екземпляри відповідних класів та скористайтеся всіма методами.
# В результаті повинно з’явитися зображення. Перегляньте їх.


import math

from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Cone(Shape):
    def draw(self):
        self.draw1.polygon([(250, 100), (200, 300), (300, 300)], fill=(23, 239, 255))
        self.draw1.ellipse((200, 280, 300, 320), fill=(12, 184, 247))

    def erase(self):
        self.draw1.polygon([(250, 100), (200, 300), (300, 300)], fill=self.back_color)
        self.draw1.ellipse((200, 280, 300, 320), fill=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-cone.png', quality=95)


class Paraboloid(Shape):
    def __init__(self):
        super().__init__()

        # Ellipse (base)
        self.x_1 = 150
        self.x_2 = 350
        self.y_1 = -200
        self.y_2 = 400

        # Rectangle (bg)
        self.y_rect_2 = (self.y_2 - math.fabs(self.y_1)) / 2

        # Ellipse (top)
        self.y_el_top_1 = self.y_rect_2 - 20
        self.y_el_top_2 = self.y_rect_2 + 20

    def draw(self):
        self.draw1.ellipse((self.x_1, self.y_1, self.x_2, self.y_2), fill=(23, 239, 255))
        self.draw1.rectangle([(self.x_1, self.y_1), (self.x_2, self.y_rect_2)], fill=self.back_color)
        self.draw1.ellipse((self.x_1, self.y_el_top_1, self.x_2, self.y_el_top_2), fill=(12, 184, 247))

    def erase(self):
        self.draw1.ellipse((self.x_1, self.y_1, self.x_2, self.y_2), fill=self.back_color)
        self.draw1.rectangle([(self.x_1, self.y_1), (self.x_2, self.y_rect_2)], fill=self.back_color)
        self.draw1.ellipse((self.x_1, self.y_el_top_1, self.x_2, self.y_el_top_2), fill=self.back_color)

    def save(self):
        print("Image with paraboloid was created")
        return self.im.save('draw-paraboloid.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(
            input(
                '\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                '\n\t9. Cтворити конус\n\t11. Cтворити параболоїд'
                '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник'
                '\n\t10. Зафарбувати конус\n\t12. Зафарбувати параболоїд\n\t'
                '8. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 9:
                c = Cone()
                work_with_obj(c)
            case 11:
                p = Paraboloid()
                work_with_obj(p)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 10:
                c = Cone()
                update_obj(c)
            case 12:
                p = Paraboloid()
                update_obj(p)
            case 8:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
