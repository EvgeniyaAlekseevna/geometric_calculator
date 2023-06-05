from abc import ABC, abstractmethod

class Figure(ABC):
    title = 'фигура'

    def __init__(self, a, call):
        super().__init__()
        self.a = a
        self.call = call

    @abstractmethod
    def square(self):
        '''площадь фигуры'''

    def print_info(self):
        '''информация о фигуре'''
        print(f"\nФигура: {self.title}")

    @abstractmethod
    def result(self):
        "вывод результатов вычисления"
