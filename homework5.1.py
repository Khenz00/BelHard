from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self):
        return self


class Dog(Animal):
    def says(self):
        return f'{self.name} - собака. Говорит ГАВ!'


class Cat(Animal):
    def says(self):
        return f'{self.name} - кот. Говорит МЯУ!!'


class Cow(Animal):
    def says(self):
        return f'{self.name} - корова. Говорит МУУ!'


d = Dog('Бобик')
ca = Cat('Барсик')
co = Cow('Буренка')
print(d.says())
print(ca.says())
print(co.says())