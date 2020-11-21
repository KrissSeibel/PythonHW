class Road:

    def __init__(self, length: float, wigth: float):
        self._length = length
        self._wigth = wigth

    def count_mass(self):
        mass = (self._length * self._wigth * 25 * 5) / 1000
        print(f"It will take {mass} ton of asphalt.")


a = Road(5000, 20)
a.count_mass()
