n = int(input())
a = []

for i in range(n):
  ox = list(input())
  sum = 0
  answer = 0
  for i in ox:
    if i == 'O':
      sum += 1
      answer += sum
    else:
      sum = 0
  a.append(answer)

for i in a:
  print(i)