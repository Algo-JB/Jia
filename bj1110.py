n = list(input())
count = 0
if len(n) == 1:
    n.insert(0, '0')  
answer = int(n[0]+n[1])
while(True):
    a = int(n[0])+int(n[1])
    n.append(str(a))
    count += 1
    if (int(n[2]) >= 10):
        n[2] = str(int(n[2]) % 10)
    test = n[-2:][0] + n[-2:][1]
    if answer == int(test):
        break
    n = list(map(str, str(test)))
    if len(n) == 1:
        n.insert(0, '0')
print(count)