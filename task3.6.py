def int_func(word):
    word = word.title()
    return word

text = input("Enter your string: ")
text = text.split()
l1 = len(text)
i = 0
j = 0
new_text = []
while i <= (l1 - 1):
    word = text[i]
    l2 = len(word)
    while j <= (l2 - 1):
        letter = word[j]
        if ord(letter) < 97 or ord(letter) > 122:
            word = None
            break
        j += 1
    if word != None:
        new_text.append(int_func(word))
    i += 1
    j = 0
new_text = " ".join(new_text)
print(new_text)
