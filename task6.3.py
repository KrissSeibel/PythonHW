class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full = " ".join([str(self.name), str(self.surname)])
        print(full)

    def get_total_income(self):
        all = self._income.get("wage") + self._income.get("bonus")
        print(all)


a = Position("John", "Johnson", "Employee", 20000, 5000)
a.get_full_name()
a.get_total_income()