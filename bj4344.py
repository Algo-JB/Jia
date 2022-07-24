c = int(input())
a = []
for _ in range(c):
  n = list(map(int, input().split()))
  avg = sum(n[1:]) / n[0]
  up = 0
  for i in range(1, n[0]+1):
    if avg < n[i]:
      up += 1
  answer = (up / n[0]) * 100
  a.append(answer)

for i in range(len(a)):
  print('%.3f' %a[i] + '%')