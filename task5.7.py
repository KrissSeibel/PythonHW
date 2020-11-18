from functools import reduce
import json

def summa(a, b):
    return a + b

dict = {}
with open("text_7.txt", "r", encoding="utf-8") as text:
    content = text.readlines()
    for el in content:
        line = el.split()
        profit = int(line[2]) - int(line[3])
        dict[line[0]] = profit
    all = reduce(summa, dict.values())
    average = all / len(dict)
    final = [dict, {"averige profit": average}]
with open("text_7.json", "w", encoding="utf-8") as new:
    json.dump(final, new)
