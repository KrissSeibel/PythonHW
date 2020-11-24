class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return abs(self.cell - other.cell)

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, n):
        one_line = chr(4041) * int(self.cell)
        if len(one_line) <= n:
            return one_line
        else:
            lines = list(one_line)
            for i in range(n, len(one_line) + 1, n +1):
                lines.insert(i, "\n")
            return "".join(lines)


a = Cell(10)
b = Cell(12)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a.make_order(4))
