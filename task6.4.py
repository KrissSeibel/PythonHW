from random import randint

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} is going!")

    def stop(self):
        print(f"Car {self.name} is stopping.")

    def turn(self):
        way = randint(0, 2)
        if way == 0:
            print(f"The car {self.name} turned right!")
        elif way == 1:
            print(f"The car {self.name} turned left!")
        else:
            print(f"The car {self.name} turned back!")

    def show_speed(self):
        print(f"Speed of car {self.name} is {self.speed} km/h.")

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Speed of car {self.name} is {self.speed}. It is more than 60 km/h!")
        else:
            print(f"Speed of car {self.name} is {self.speed}")

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Speed of car {self.name} is {self.speed}. It is more than 40 km/h!")
        else:
            print(f"Speed of car {self.name} is {self.speed}")

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


volvo = TownCar(55, "blue", "Volvo", False)
ferrary = SportCar(200, "red", "Ferrary", False)
belaz = WorkCar(50, "orange", "BelAz", False)
bmw = PoliceCar(100, "white", "BMW")

volvo.go()
volvo.turn()
volvo.turn()
volvo.turn()
volvo.show_speed()
volvo.stop()

ferrary.go()
ferrary.turn()
ferrary.turn()
ferrary.turn()
ferrary.show_speed()
ferrary.stop()

belaz.go()
belaz.turn()
belaz.turn()
belaz.turn()
belaz.show_speed()
belaz.stop()

bmw.go()
bmw.turn()
bmw.turn()
bmw.turn()
bmw.show_speed()
bmw.stop()
