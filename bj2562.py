num = []
for i in range(9):
    n = int(input())
    num.append(n)

maxN = max(num)
for i in range(9):
    if num[i] == maxN:
        print(maxN)
        print(i+1)
        
