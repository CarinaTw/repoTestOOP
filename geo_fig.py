'''
    Создать класс геометрической фигуры.
    Реализовать на его основе классы фигур Треугольник, Прямоугольник, Квадрат, Круг.

    1 Часть.
    Фигура должна иметь атрибуты:
    name - название фигуры,
    area - выводить площадь,
    angles - выводить количество углов
    perimeter - выводить периметр (сумму длин сторон, длину окружности)

    Фигура должна реализовать метод add_square() который должен принимать другую фигуру и выводить сумму площадей
    этих фигур.
    Если передана не геометрическая фигура, то нужно выдавать ошибку и сообщать что передан неправильный класс.

    2. Часть.
    Написать тесты с использованием pytest на эти классы.
    По одному тесту на каждый метод каждой фигуры. Т.е. будет четыре тестовых модуля по 5 тестов на каждый.
    Можно написать и больше. :)


    Задача: Потренировать объектно-ориентированное мышление, и написание тестов на собственный код.

    Критерии оценки: Будет оцениваться глубина использования парадигмы ООП. Встроенные декораторы, наследование,
    отсутствие дублирования кода. Если какой-то метод выполняет одно и тоже во всех классах наследниках,
    то он должен принадлежать родтельскому классу.
'''

import math


class GeometricFigure:
    def __init__(self):
        self.area = 0

    def set_name(self):
        self.name = self.__class__.__name__

    def get_name(self):
        return self.name

    def set_angles(self):
        if self.name in ('Square', 'Rectangle'):
            self.angles = 4
        elif self.name == 'Triangle':
            self.angles = 3
        elif self.name == 'Cyrcle':
            self.angles = 0

    def get_angles(self):
        print('Count of angles = ' + str(self.angles))
        return self.angles

    def set_perimeter(self, *args):
        if self.angles == 4:
            a, b = args
            self.perimeter = (a + b) * 2
        elif self.angles == 0:
            self.perimeter = 2 * math.pi * args[0]

    def get_perimeter(self):
        print('Perimeter = ' + str(self.perimeter))
        return self.perimeter

    def get_area(self):
        return self.area

    def add_square(self, figure_obj):
        assert figure_obj.get_name() in ('Square', 'Rectangle', 'Triangle', 'Cyrcle'), 'Not a geometric figure!'
        area1 = self.area
        area2 = figure_obj.get_area()
        sum =  area1 + area2
        print('Area 1 = ' + str(area1) + ' Area 2 = ' + str(area2) + ' and their sum = ' + str(sum))
        return sum


class Rectangle(GeometricFigure):
    def __init__(self, a, b):
        self.set_name()
        self.a_side_len = a
        self.b_side_len = b
        self.set_area()
        self.set_angles()
        self.set_perimeter(a, b)
        print('This is Rectangle: side A=' + str(a) + ' and side B=' + str(b))

    def set_area(self):
        self.area = self.a_side_len * self.b_side_len
        print('Area of figure = ' + str(self.area))


class Square(Rectangle):
    def __init__(self, a):
        self.set_name()
        self.a_side_len = a
        self.b_side_len = self.a_side_len
        self.set_area()
        self.set_angles()
        self.set_perimeter(self.a_side_len, self.b_side_len)
        assert type(self.a_side_len) == int, 'Type must be INT'
        print('This is Square: sides A,B,C,D=' + str(a))


class Triangle(GeometricFigure):
    def __init__(self, a, b, c):
        self.set_name()
        self.a_side_len = a
        self.b_side_len = b
        self.c_side_len = c
        self.set_angles()
        self.set_area()

        assert type(self.a_side_len)==type(self.b_side_len)==type(self.c_side_len)==int, 'Type must be INT'
        print('This is Triangle: side A=' + str(a) + ' side B=' + str(b) + ' and side C=' + str(c))

    def set_area(self):
        p = (self.a_side_len + self.b_side_len + self.c_side_len)/2
        self.area = math.sqrt(p*(p - self.a_side_len) * (p - self.b_side_len) * (p - self.c_side_len))
        print('Area of figure = ' + str(self.area))
        #return self.area


class Cyrcle(GeometricFigure):
    def __init__(self, a):
        self.set_name()
        self.cyrcl_rad = a
        self.set_angles()
        self.set_perimeter(a)
        self.set_area()

        assert type(self.cyrcl_rad) == int, 'Type must be INT'
        print('This is Cyrcle: cyrcle radius=' + str(a))

    def set_area(self):
        self.area = math.pi * self.cyrcl_rad**2
        print('Area of figure = ' + str(self.area))

    def get_area(self):
        return round(self.area, 3)

    def add_square(self, figure_obj):
        assert figure_obj.get_name() in ('Square', 'Rectangle', 'Triangle', 'Cyrcle'), 'Not a geometric figure!'
        area1 = self.area
        area2 = figure_obj.get_area()
        sum =  area1 + area2
        print('Area 1 = ' + str(area1) + ' Area 2 = ' + str(area2) + ' and their sum = ' + str(round(sum,3)))
        return round(sum, 3)


# rect = Rectangle(10,5)
# rect.get_name()
# rect.get_area()
# rect.get_angles()
# rect.get_perimeter()

# sq = Square(5)
# rect.add_square(sq)
#
# print('-'*150)
#
# sq = Square(5)
# sq.get_name()
# sq.get_area()
# sq.get_angles()
# sq.get_perimeter()
#
# print('-'*150)
#
# tr = Triangle(3, 4, 5)
# tr.get_name()
# tr.get_area()
# tr.get_angles()
#
# print('-'*150)
#
# cyr = Cyrcle(3)
# cyr.get_name()
# cyr.get_area()
# cyr.get_angles()
# cyr.get_perimeter()
#
# print('='*150)
#
# rect2 = Rectangle(2, 4)
# # sq.add_square(rect2)
# #
# sq2 = Square(6)
# rect2.add_square(sq2)