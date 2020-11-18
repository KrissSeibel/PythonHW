with open("text_2.txt", encoding="utf-8") as text:
    content = text.readlines()
    j = 1
    for i in content:
        line = i.split()
        c_words = len(line)
        print(f"In line {j} number {c_words} words.")
        j += 1
    print(f"Number of lines: {j - 1}.")