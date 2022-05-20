class Car:

    __speed=int
    __model=str
    __year_issue=int
    __mark=str
    def __init__(self,mark,year_issue,model,speed=0):
        self.__speed=speed
        self.__mark=mark
        self.__model=model
        self.__year_issue=year_issue
    def speed_up(self):
        return self.__speed+5
    def speed_down(self):
        return self.__speed-5
    def speed_current(self):
        return self.__speed
    def stop(self):
        return self.__speed-self.__speed
    def reverse(self):
        return self.__speed-self.__speed*2





c=Car('Audi','1995','A5',20)
print(c.speed_up())
print(c.speed_down())
print(c.speed_current())
print(c.stop())
print(c.reverse())