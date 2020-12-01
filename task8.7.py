class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (self.a + other.a) + (self.b + other.b) * 1j

    def __mul__(self, other):
        return (self.a * other.a - self.b * other.b) + (self.b * other.a + self.a * other.b) * 1j


c_1 = Complex(1, 2)
c_2 = Complex(3, 4)
print(c_1 * c_2)
print(c_1 + c_2)
