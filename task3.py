n = int(input("Enter number: "))
a = 1
i = 0
if n < 0:
    print("Error!")
else:
    while a > 0:
        i += 1
        a = n // (10 ** i)
    summa = (100 ** i) * n + 2 * (10 ** i) * n + 3 * n
    print(summa)