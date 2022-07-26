from re import I


x = int(input())
i = 1
while(x >= 0):
  x -= i
  if x < 0:
    x += i
    i -=1
    break
  i += 1

if i % 2 == 1:
  if x == 0:
    print('%d/%d' %(1,i))
  else:
    m = (i+1) - (x-1)
    j = x
    print('%d/%d' %(j,m))
else:
  if x == 0:
    print('%d/%d' %(i,1))
  else:
    m = x
    j = (i+1) - (x-1)
    print('%d/%d' %(j,m))