rating = [7, 5, 3, 3, 2]
x = int(input("Enter new element fer rating: "))
l = len(rating)
a = rating[l - 1]
i = 0
if x <= a:
    rating.append(x)
else:
    while i <= l:
        if x > rating[i]:
            rating.insert(i, x)
            break
        else:
            i += 1
print(rating)