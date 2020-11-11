def my_func(a, b, c):
    if a == b or b == c or a == c:
        return "No single minimal value."
    else:
        minimal = min([a, b, c])
        summa = sum([a, b, c]) - minimal
        return f"Summa: {summa}."

while True:
    try:
        print(my_func(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))
        break
    except ValueError:
        print("ValueError! Please, try again.")