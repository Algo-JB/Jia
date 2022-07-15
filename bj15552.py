import sys
n = int(input())
answer = []

for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        answer.append(a + b)
for i in range(n):
    print(answer[i])
