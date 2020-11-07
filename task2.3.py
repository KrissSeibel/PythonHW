year = {1: "January, Winter", 2: "February, Winter", 3: "March, Spring",
        4: "April, Spring", 5: "May, Spring",6: "June, Summer", 7: "July, Summer",
        8: "August, Summer", 9: "September, Autumn", 10: "October, Autumn", 11: "November, Autumn",
        12: "December, Winter"}

while True:
    month = input("Enter month number (1 - 12): ")
    if not month.isdigit():
        print("That's not right, dude!")
    else:
        month = int(month)
        if month >= 1 and month <= 12:
            x = year.get(month)
            print(x)
            break
        else:
            print("Wrong number entered!")