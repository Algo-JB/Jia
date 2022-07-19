c = []
while True:
    try:
        a, b = map(int, input().split())
        c.append(a +b)
    except:
        for i in range(len(c)):
            print(c[i])
        break