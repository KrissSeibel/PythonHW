my_list = input("Enter list items separated by space: ")
my_list = my_list.split()
a = len(my_list) // 2 * 2
for i in range(0, a, 2):
    even = my_list[i]
    uneven = my_list[i + 1]
    my_list[i] = uneven
    my_list[i + 1] = even
print(my_list)
