a = int(input("Result of the first day: "))
b = int(input("Desired result: "))
if a < 0 or b < 0:
    print("Error!")
else:
    i = 1
    while a < b:
        a = a * 1.1
        i += 1
    print(f"The desired result will be achieved on day {i}.")
