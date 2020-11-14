def calc():
    try:
        from sys import argv
        name, hours, rate, bonus = argv
        try:
            wages = int(hours) * int(rate) + int(bonus)
            return wages
        except ValueError:
            print("ValueError!")
    except ValueError:
        return "Parameters not found!"



print(calc())
