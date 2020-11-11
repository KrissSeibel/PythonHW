def my_func():
    while True:
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            if x > 0 and y < 0:
                break
            else:
                print("Incorrect data. Please, try again.")
        except ValueError:
            print("ValueError! Please, try again.")
    result = 1
    while y < 0:
        result = result / x
        y += 1
    return f"Result: {result:.3f}"


print(my_func())
