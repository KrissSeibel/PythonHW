def function(a, b):
    try:
        quotient = a / b
        print(f"Quotient: {quotient:.3f}")
    except ZeroDivisionError:
        print("ZeroDivisionError!")
while True:
    try:
        function(int(input("Enter a: ")), int(input("Enter b: ")))
        break
    except ValueError:
        print("Error! Please, try again.")
