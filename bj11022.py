t = int(input())
rst = []
aL = []
bL = []

for i in range(t):
    a, b = map(int, input().split())
    aL.append(a)
    bL.append(b)
    rst.append(a + b)

for i in range(t):
    print('Case #%s: %s + %s = %s' %(i+1, aL[i], bL[i], rst[i]))
