class Car:

    speed=int
    model=str
    year_issue=int
    name=str
    def __init__(self,speed=0):
        self.speed=speed
    def __iter__(self):
        return self
    def __next__(self):
        speed = self.speed
        self.speed +=5
        return speed
    def speed_up(self):
        speed = self.speed
        self.speed+=5
        return speed
    def speed_down(self):
        speed=self.speed
        self.speed-=5
        return speed
    def speed_current(self):
        speed=self.speed
        return speed
    def stop(self):
        speed=self.speed
        speed*=0
        return speed





c=Car()
print(c.speed_up())
print(c.speed_up())
print(c.speed_down())
print(c.speed_current())
print(c.stop())
