import math
from figure import Figure
from abc import ABC, abstractmethod



class VoluminousFigures(Figure, ABC):
    title = "объёмные фигуры"

    @abstractmethod
    def volume(self):
        '''объём фигуры'''

    @staticmethod
    def calculations_VoluminousFigures():
        print("Вычислить: \n- площадь - объём")

    def result(self):
        self.print_info()
        if self.call == "объём":
            print("объём =", self.volume())
        elif self.call == "площадь":
            print("площадь =", self.square())
        else:
            print("объём =", self.square())
            print("площадь =", self.volume())


class Sphere(VoluminousFigures):
    title = "сфера"

    def print_info(self):
        super().print_info()
        print(f"радиус = {self.a}")

    def square(self):
        return round((4 * math.pi * self.a ** 2), 2)

    def volume(self):
        return round((4 / 3 * math.pi * self.a ** 3), 2)


class Cube(VoluminousFigures):
    title = "куб"

    def print_info(self):
        super().print_info()
        print(f"сторона a = {self.a}")

    def square(self):
        return 6 * self.a ** 2

    def volume(self):
        return self.a ** 3


class Parallelepiped(Cube):
    title = "параллелепипед"

    def __init__(self, a, b, h, call):
        super().__init__(a, call)
        self.b = b
        self.h = h

    def print_info(self):
        super().print_info()
        print(f"сторона b = {self.b}")
        print(f"высота h = {self.h}")

    def square(self):
        return 2 * (self.a * self.b + self.a * self.h + self.b * self.h)

    def volume(self):
        return round((4 / 3 * math.pi * self.a ** 3), 2)


class Pyramid(Parallelepiped):
    title = "пирамида"

    def __init__(self, n, a, b, h, call):
        super().__init__(a, b, h, call)
        self.n = n

    def print_info(self):
        super().print_info()
        print(f"граней n = {self.n}")

    def square(self):
        '''
        if self.n == 3:
            S_osn = ((self.a ** 2) * (3 ** 0.5)) / 4
            S_bok = (3 * self.a * ((self.b ** 2 - (self.a ** 2) / 4) ** 0.5)) / 2
            return round((S_osn + S_bok), 2)
        elif self.n == 4:
            S_osn = self.a ** 2
            S_bok = 2 * self.a * ((self.b ** 2 - (self.a ** 2) / 4) ** 0.5)
            return round((S_osn + S_bok), 2)
        elif self.n == 6:
            S_osn = (3 * (3 ** 0.5) * (self.a ** 2)) / 2
            S_bok = 3 * self.a * ((self.b ** 2 - (self.a ** 2) / 4) ** 0.5)
            return round((S_osn + S_bok), 2)
        else:
        '''
        return "расчёт не найден"

    def volume(self):
        '''
        if self.n == 3:
            return round(((3 ** 0.5) * (self.a ** 2) * self.h), 2)
        elif self.n == 4:
            return round((1 / 3 * (self.a ** 2) * self.h), 2)
        elif self.n == 6:
            return round(((3 * (3 ** 0.5) * (self.a ** 2) * self.h) / 6), 2)
        else:
        :return:
        '''
        return "расчёт не найден"


class Cylinder(Sphere):
    title = "цилиндр"

    def __init__(self, a, h, call):
        super().__init__(a, call)
        self.h = h

    def print_info(self):
        super().print_info()
        print(f"высота h = {self.h}")

    def square(self):
        return round((2 * math.pi * self.a * (self.a + self.h)), 2)

    def volume(self):
        return round((math.pi * self.a ** 2 * self.h), 2)


class Cone(Cylinder):
    title = "конус"

    def formingACone(self):
        return (self.a ** 2 + self.h ** 2) ** 0.5

    def square(self):
        l = Cone.formingACone(self)
        return round((math.pi * self.a * (self.a + l)), 2)

    def volume(self):
        return round((1 / 3 * math.pi * self.a ** 2 * self.h), 2)
