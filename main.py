from flatFigures import *
from voluminousFigures import *
print("Геометрический калькулятор плоских и объёмных фигур")

list_FlatFigures = ['круг', 'квадрат', 'прямоугольник', 'треугольник', 'трапеция', 'ромб']
print(f"Плоские фигуры: ")
for i in list_FlatFigures:
    print(" -", i, end="")
print()
list_VoluminousFigures = ['сфера', 'куб', 'параллелепипед', 'пирамида', 'цилиндр', 'конус']
print(f"Объёмные фигуры: ")
for i in list_VoluminousFigures:
    print(" -", i, end="")
print()

figure_name = input("Введите название геометрической фигуры: ")

while True:
    try:
        if figure_name in list_FlatFigures:
            FlatFigures.calculations_FlatFigures()
            call = input("Вычислить: ")
            match figure_name:
                case "круг":
                    r = int(input("Введите радиус круга: "))
                    circle = Circle(r, call)
                    circle.result()
                case "квадрат":
                    a = int(input("Введите длину стороны: "))
                    square = Square(a, call)
                    square.result()
                case "прямоугольник":
                    a = int(input("Введите длину стороны a : "))
                    b = int(input("Введите длину стороны b : "))
                    rectangle = Rectangle(a, b, call)
                    rectangle.result()
                case "треугольник":
                    a = int(input("Введите длину стороны a : "))
                    b = int(input("Введите длину стороны b : "))
                    c = int(input("Введите длину стороны c : "))
                    triangle = Triangle(a, b, c, call)
                    triangle.result()
                case "трапеция":
                    a = int(input("Введите длину основания a : "))
                    b = int(input("Введите длину стороны b : "))
                    c = int(input("Введите длину стороны c : "))
                    d = int(input("Введите длину стороны d : "))
                    trapezoid = Trapezoid(a, b, c, d, call)
                    trapezoid.result()
                case "ромб":
                    a = int(input("Введите длину стороны a : "))
                    h = int(input("Введите высоту h : "))
                    rhombus = Rhombus(a, h, call)
                    rhombus.result()
        elif figure_name in list_VoluminousFigures:
            VoluminousFigures.calculations_VoluminousFigures()
            call = input("Вычислить: ")
            match figure_name:
                case "сфера":
                    r = int(input("Введите радиус круга: "))
                    sphere = Sphere(r, call)
                    sphere.result()
                case "куб":
                    a = int(input("Введите длину стороны a : "))
                    cube = Cube(a, call)
                    cube.result()
                case "параллелепипед":
                    a = int(input("Введите длину стороны a : "))
                    b = int(input("Введите длину стороны b : "))
                    h = int(input("Введите высоту h : "))
                    parallelepiped = Parallelepiped(a, b, h, call)
                    parallelepiped.result()
                case "пирамида":
                    #a = int(input("Введите длину стороны основания a : "))
                    #b = int(input("Введите длину граней b : "))
                    #n = int(input("Введите количество граней n : "))
                    #h = int(input("Введите высоту h : "))
                    #pyramid = Pyramid(n, a, b, h, call)
                    #pyramid.result()
                    print("Вычисления для данной фигуры не найдены")
                case "цилиндр":
                    a = int(input("Введите радиус основания r : "))
                    h = int(input("Введите высоту h : "))
                    cylinder = Cylinder(a, h, call)
                    cylinder.result()
                case "конус":
                    a = int(input("Введите радиус основания r : "))
                    h = int(input("Введите высоту h : "))
                    cone = Cone(a, h, call)
                    cone.result()
        else:
            print("фигура не распознана")
    except:
        print("Ошибка ввода данных!")

    perform = input("Выполнить ещё раз геометрический расчёт? (да/нет): ")
    if perform == "да":
        figure_name = input("Введите название геометрической фигуры: ")
    elif perform == "нет":
        print("Программа завершена")
        break
    else:
        print("Ответ не распознан")
        perform = input("Выполнить ещё раз геометрический расчёт? (да/нет): ")
        if perform == "да":
            figure_name = input("Введите название геометрической фигуры: ")
        elif perform == "нет":
            print("Программа завершена")
            break
        else:
            print("Ответ не распознан. Программа завершена")
            break