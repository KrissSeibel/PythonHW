from itertools import count, cycle


def generator():
    for el in count(3):
        if el > 10:
            break
        print(el)
        yield el


i = 0
for el in cycle(list(generator())):
    if i > 15:
        break
    print(el)
    i += 1