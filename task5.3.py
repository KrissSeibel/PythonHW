with open("text_3.txt", encoding="utf-8") as text:
    content = text.readlines()
    l = len(content)
    summa = 0
    for line in content:
        person = line.split()
        x = float(person[1])
        if x < 20000.0:
            print(f"{person[0]}'s salary is less then 20000")
        summa += x
    print(f"Avarage salary: {summa / l}.")

