class MyError(Exception):
    def __init__(self, smth):
        self.smth = smth


list_of_numbers = []
while True:
    x = input("Enter number. To close the program enter 'Stop'. ").title()
    if x == "Stop":
        break
    else:
        try:
            y = x.isdigit()
            if y == False:
                raise MyError("Incorrect data. Only numbers!")
        except MyError as err:
            print(err)
        else:
            list_of_numbers.append(int(x))
print(list_of_numbers)