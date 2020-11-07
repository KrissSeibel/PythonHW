string = input("Enter your string: ")
string_list = string.split()
for i in enumerate(string_list):
    if len(i[1]) <= 10:
        print(i)
    else:
        print(i[1][:10])

