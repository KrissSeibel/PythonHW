rev = int(input("Enter your revenue: "))
exp = int(input("Enter your expenses: "))
dif = rev - exp
if dif > 0:
    print(f"Your company have made a profit. Your cost effectiveness is {dif / rev * 100:.2f} %.")
    labor = int(input("How many people are working in your company? "))
    print(f"One employee have earned {dif / labor:.2f} profit for your company.")
if dif < 0:
    print("Your company is incurring losses.")
if dif == 0:
    print("Your company is operating at zero.")
