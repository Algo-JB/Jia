n = int(input())
answer = []
for i in range(n):
    num1, num2 = map(int, input().split())
    answer.append(num1+num2)

for i in range(n):
    print(answer[i])