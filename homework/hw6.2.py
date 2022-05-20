class Car:
    def __init__(self,color,mark,speed):
        self.__color=color
        self.__mark=mark
        self.__speed=speed
    def parameters(self):
        return (f'Основные характеристики авто {self.__mark},{self.__color} и макс скорость {self.__speed}')
