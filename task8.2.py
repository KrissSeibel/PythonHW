class MyZeroError(Exception):
    def __init__(self, smth):
        self.smth = smth


x = input("Enter first number: ")
y = input("Enter second number: ")
try:
    x = int(x)
    y = int(y)
    if y == 0:
        raise MyZeroError("You can't divide by zero.")
except (ValueError, MyZeroError) as err:
    print(err)
else:
    print(f"The result of division is {x / y:.2f}.")