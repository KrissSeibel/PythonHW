class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Start of drawing with {self.title} color.")

class Pen(Stationery):

    def draw(self):
        print(f"Start of drawing with {self.title} Pen!")

class Pencil(Stationery):

    def draw(self):
        print(f"Start of drawing with {self.title} Pencil!")

class Handle(Stationery):

    def draw(self):
        print(f"Start of drawing with {self.title} Handle!")


pen = Pen("red")
pen.draw()
pencil = Pencil("blue")
pencil.draw()
handle = Handle("yellow")
handle.draw()