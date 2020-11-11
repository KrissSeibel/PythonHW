def my_func1():
    summa = 0
    while True:
        try:
            print("Enter numbers separated space.", "To exit the programm, enter 'Q': ", sep="\n")
            num = input()
            if num.upper() == "Q":
                print(summa)
                break
            num = num.split()
            l = len(num)
            if num[l - 1].upper() == "Q":
                num.pop()
                for i in num:
                    summa = summa + int(i)
                print(summa)
                break
            else:
                for i in num:
                    summa = summa + int(i)
                print(summa)
        except ValueError:
            print("ValueError! Please, try again.")



my_func1()












