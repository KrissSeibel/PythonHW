def fact(n):
    result = 1
    try:
        if int(n) == 0:
            print(1)
        elif int(n) < 0:
            print("The factorial can only be calculated for a non-negative number.")
        else:
            for i in range(1, int(n) + 1):
                result = result * i
                yield result
    except TypeError:
        print("TypeError!")
    except ValueError:
        print("ValueError!")


for el in fact(input("Enter n: ")):
    print(el)
