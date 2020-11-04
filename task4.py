num = int(input("Enter number: "))
i = 1
a = 0
if num < 0:
    num = num * -1
while (num // 10 ** (i - 1)) > 0:
    x = (num % (10 ** i)) // (10 ** (i - 1))
    if x > a:
        a = x
    i += 1
print("The biggest number is {}.".format(a))
