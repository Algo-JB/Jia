number = list(range(1, 10001))
g_number = []

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  if i <= 10000:
    g_number.append(i)

for g_number in set(g_number):
  number.remove(g_number)
for i in number:
  print(i)