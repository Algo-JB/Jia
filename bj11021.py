t = int(input())
rst = []

for i in range(t):
    a, b = map(int, input().split())
    rst.append(a + b)

for i in range(t):
    print('Case #%s: %s' %(i+1, rst[i]))
