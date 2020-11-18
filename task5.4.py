er_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", encoding="utf-8") as text:
    lines = text.readlines()
    for line in lines:
        one = line.split()
        key = one[0]
        one[0] = er_dict.get(key)
        new_line = " ".join(one)
        with open("text_4.1.txt", "a", encoding="utf-8") as new_text:
            new_text.write(f"{new_line}\n")
