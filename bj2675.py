t = int(input())
textL = []
for i in range(t):
    r, s = map(str, input().split())
    text = ''
    for i in s:
        text += int(r) * i

    textL.append(text)
for i in textL:
    print(i)
