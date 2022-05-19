class Car:
    global speed
    speed=
    model=str
    year_issue=int
    name=str
    def __init__(self,speed=[]):
        self.speed=speed
    def speed_up(self):
        return (self.speed+5)
    def speed_down(self):
        return self.speed-5
    def stop(self):
        return self.speed
    def speed_current(self):
        return self.speed





c=Car()
print(c.speed_up())