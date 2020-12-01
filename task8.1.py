class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls):
        return [int(num) for num in Date(input("Enter date: ")).date.split("-")]


    @staticmethod
    def validation():
        date_list = Date.to_int()
        list_31 = [1, 3, 5, 7, 8, 10, 12]
        list_30 = [4, 6, 9, 11]
        if date_list[1] in list_31:
            if 1 <= date_list[0] <= 31:
                return "Correct date."
            else:
                return "Incorrect date."
        elif date_list[1] in list_30:
            if 1 <= date_list[0] <= 30:
                return "Correct date."
            else:
                return "Incorrect date."
        elif date_list[1] == 2:
            if date_list[2] % 4 != 0 or date_list[2] % 100 == 0 and date_list[2] % 400 != 0:
                if 1 <= date_list[0] <= 28:
                    return "Correct date."
                else:
                    return "Incorrect date."
            else:
                if 1 <= date_list[0] <= 29:
                    return "Correct date."
                else:
                    return "Incorrect date."
        else:
            return "Incorrect date."


print(Date.validation())