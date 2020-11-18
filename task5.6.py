dict = {}
with open("text_6.txt", "r", encoding="utf-8") as text:
    content = text.readlines()
    for el in content:
        line = el.split()
        gen = 0
        for word in line:
            lessons = ""
            for i in range(len(word)):
                if word[i].isdigit():
                    lessons = "".join([lessons, word[i]])
            if lessons != "":
                lessons = int(lessons)
                gen += lessons
        if gen != 0:
            dict[line[0]] = gen
    print(dict)