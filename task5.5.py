from random import randint
from functools import reduce

numbers = [randint(0, 50) for _ in range(randint(3, 10))]
numbers_str = []
for i in numbers:
    numbers_str.append(str(i))
new = " ".join(numbers_str)
with open("text_5.txt", "w", encoding="utf-8") as nums:
    nums.write(new)

with open("text_5.txt", "r", encoding="utf-8") as nums:
    content = nums.read()
    list_nums = content.split()
    new_list = [int(num) for num in list_nums]

    def my_func(el1, el2):
        return el1 + el2

    print(reduce(my_func, new_list))