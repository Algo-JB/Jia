n = int(input())
count = 0

for i in range(1, n + 1):
  answer = list(map(int, str(i)))
  if i < 100:
    count += 1
  elif answer[2] - answer[1] == answer[1] - answer[0]:
    count += 1

print(count)
