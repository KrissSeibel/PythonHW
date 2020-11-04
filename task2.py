t = int(input("Enter time in seconds:  "))
if t < 0:
    print("Error!")
else:
    if t < 3600:
        h1 = 0
        h2 = 0
    else:
        h1 = t // 36000
        h2 = t // 3600 - h1 * 10
    if t < 60:
        m1 = 0
        m2 = 0
    else:
        tm = t // 60 - (h1 * 10 + h2) * 60
        m1 = tm // 10
        m2 = tm % 10
    s2 = t % 10
    s1 = (t % 60 - s2) / 10
    print("%d%d:%d%d:%d%d" % (h1, h2, m1, m2, s1, s2))
