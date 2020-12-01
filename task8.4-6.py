from abc import abstractmethod


class Storage:
    def __init__(self):
        self.storage = {}

    def incoming(self, item, count):

        if count.isdigit():
            count = int(count)
            if item.__str__() in self.storage:
                self.storage[item.__str__()] = self.storage[item.__str__()] + count
            else:
                self.storage[item.__str__()] = count
            return f"\n{count} of {item.__str__()} came to the storage.\n"
        else:
            return "Quantity must be a number."

    def outcoming(self, item, count, department):
        if count.isdigit():
            count = int(count)
            if item.__str__() in self.storage and count <= self.storage[item.__str__()]:
                self.storage[item.__str__()] = self.storage[item.__str__()] - count
                return f"\n{count} of {item.__str__()} were moved to the {department}.\n"
            else:
                return f"\nThere are no items to moving to the {department}.\n"
        else:
            return "Quantity must be a number."

    def list(self):
        list = []
        for i in self.storage:
            list.append(f"{i} : {self.storage[i]}")
        return "\n".join(list)


class OfficeEquipment:
    def __init__(self, producer, model):
        self.producer = producer
        self.model = model

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, producer, model, print_options):
        super().__init__(producer, model)
        self.print_options = print_options

    def __str__(self):
        return f"Printer {self.producer} {self.model} {self.print_options}"


class Scanner(OfficeEquipment):
    def __init__(self, producer, model, scanner_type):
        super().__init__(producer, model)
        self.scanner_type = scanner_type

    def __str__(self):
        return f"Scanner {self.producer} {self.model} {self.scanner_type}"


class Xerox(OfficeEquipment):
    def __init__(self, producer, model, functionality):
        super().__init__(producer, model)
        self.functionality = functionality

    def __str__(self):
        return f"Xerox {self.producer} {self.model} {self.functionality}"


p_1 = Printer("HP", "LaserJet" , "Duplex printing")
p_2 = Printer("Canon", "i-SENSYS LBP1" , "Single-sided printing")
s_1 = Scanner("HP", "ScanJet Pro 3500" , "Digital")
s_2 = Scanner("Canon", "CanoScan LiDE 400" , "Analog")
x_1 = Xerox("Xerox", "VersaLink C400DN" , "Special")
x_2 = Xerox("Epson", "L3050" , "Standart")

dict = {"1": p_1, "2": p_2, "3": s_1, "4": s_2, "5": x_1, "6": x_2}
store = Storage()


def create():
    while True:
        print("For create new printer enter 'P'.\nFor create new scaner enter 'S'.\nFor create new xerox enter 'X'.\n"
              "For return to previous menu enter 'Q': ")
        y = input().title()
        if y == "Q":
            break
        elif y == "P":
            dict[str(len(dict) + 1)] = Printer(input("Enter producer: "), input("Enter model: "),
                                               input("Enter print options: "))
        elif y == "S":
            dict[str(len(dict) + 1)] = Scanner(input("Enter producer: "), input("Enter model: "),
                                               input("Enter scanner type: "))
        elif y == "X":
            dict[str(len(dict) + 1)] = Xerox(input("Enter producer: "), input("Enter model: "),
                                             input("Enter functionality: "))
        else:
            print("\nError! Please, try again.\n")


def add():
    for i in dict:
        print(f"{i}: {dict[i]}")
    while True:
        item_id = input("Choose the item by ID: ")
        if item_id in dict:
            confirm = input(f"You have chosen {dict[item_id]}. To confirm enter 'Y', else enter nothing: ").title()
            if confirm == "Y":
                break
        else:
            print("\nID is incorrect. Please, try again.\n")
    while True:
        co = input("Enter quantity of item: ")
        if co.isdigit():
            break
        else:
            print("\nQuantity must be only a number. Please, try again.\n")
    print(store.incoming(dict[item_id], co))


def move():
    for i in dict:
        print(f"{i}: {dict[i]}")
    while True:
        item_id = input("Choose the item by ID: ")
        if item_id in dict:
            if input(f"You have chosen {dict[item_id]}. To confirm enter 'Y', else enter nothing: ").title() == "Y":
                break
        else:
            print("\nID is incorrect. Please, try again.\n")
    while True:
        co = input("Enter quantity of item: ")
        if co.isdigit():
            break
        else:
            print("\nQuantity must be only a number. Please, try again.\n")
    while True:
        dep = input("Enter department to move an item: ")
        if input(f"You have chosen {dep} to move an item. To confirm enter 'Y', else enter nothing: ").title() == "Y":
            break
    print(store.outcoming(dict[item_id], co, dep))


while True:
    print("For create new item enter 'C'.\nFor add an item to storage enter 'A'.\nFor move item to department enter 'M'.\n"
          "For looking through the storage enter 'L'.\nFor close the program enter 'Q': ")
    x = input().title()
    if x == "Q":
        break
    if x == "C":
        create()
    if x == "A":
        add()
    if x == "M":
        move()
    if x == "L":
        if len(store.list()) > 0:
            print(store.list())
        else:
            print("\nStorage is empty. At first, add items to it.\n")