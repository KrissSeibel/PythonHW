from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption_textile(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def consumption_textile(self):
        return f"To sew a coat, you need {self.v / 16.5 + 0.5:.2f} meters of textile."


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def consumption_textile(self):
        return f"To sew a costume, you need {self.h * 2 + 0.3:.2f} meters of textile."


c = Coat(46)
print(c.consumption_textile)
co = Costume(1.70)
print(co.consumption_textile)