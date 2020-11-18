object = open("text_1.txt", "w", encoding="utf-8")
i = 0
while True:
    line = input("Enter your string: ")
    if line == "":
        break
    object.writelines(f"{line}\n")
    i += 1
object.close()
