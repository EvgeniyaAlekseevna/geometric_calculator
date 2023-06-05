import math
from figure import Figure
from abc import ABC, abstractmethod



class FlatFigures(Figure, ABC):
    title = "плоские фигуры"

    @abstractmethod
    def perimeter(self):
        '''периметр фигуры'''

    @staticmethod
    def calculations_FlatFigures():
        print("Вычислить: \n- периметр - площадь")

    def result(self):
        self.print_info()
        if self.call == "периметр":
            print("периметр =", self.perimeter())
        elif self.call == "площадь":
            print("площадь =", self.square())
        else:
            print("периметр =", self.perimeter())
            print("площадь =", self.square())


class Circle(FlatFigures):
    title = "круг"

    def print_info(self):
        super().print_info()
        print(f"радиус = {self.a}")

    def perimeter(self):
        return round((2 * math.pi * self.a), 2)

    def square(self):
        return round((math.pi * self.a ** 2), 2)


class Square(FlatFigures):
    title = "квадрат"

    def print_info(self):
        super().print_info()
        print(f"сторона a = {self.a}")

    def perimeter(self):
        return self.a * 4

    def square(self):
        return self.a ** 2


class Rectangle(Square):
    title = "прямоугольник"

    def __init__(self, a, b, call):
        super().__init__(a, call)
        self.b = b

    def print_info(self):
        super().print_info()
        print(f"сторона b = {self.b}")

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b


class Triangle(Rectangle):
    title = "треугольник"

    def __init__(self, a, b, c, call):
        super().__init__(a, b, call)
        self.c = c

    def print_info(self):
        super().print_info()
        print(f"сторона c = {self.c}")

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        try:
            return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)
        except:
            return "Такого треугольника нет!"


class Trapezoid(Triangle):
    title = "трапеция"

    def __init__(self, a, b, c, d, call):
        super().__init__(a, b, c, call)
        self.d = d

    def print_info(self):
        super().print_info()
        print(f"сторона d = {self.d}")

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        if self.a - self.b != 0:
            return round((((self.a + self.b) / 2) * (self.c ** 2 - (
                    ((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) /
                    (2 * (self.a - self.b))) ** 2) ** 0.5)
                                      , 2)
        else:
            return "Такой трапеции не существует!"


class Rhombus(Square):
    title = "ромб"

    def __init__(self, a, h, call):
        super().__init__(a, call)
        self.h = h

    def print_info(self):
        super().print_info()
        print(f"высота h = {self.h}")

    def square(self):
        return self.a * self.h
