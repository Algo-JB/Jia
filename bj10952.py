listA = []
listB = []
while (1):
    a, b = map(int, input().split())
    listA.append(a)
    listB.append(b)
    if a == 0 and b == 0:
        break

for i in range(len(listA)-1):
    print(listA[i]+listB[i])