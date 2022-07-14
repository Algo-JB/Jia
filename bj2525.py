a, b = map(int, input().split())
c = int(input()) 

ap = int((b + c) / 60) + a
bp = (b + c) % 60

if ap >= 24:    
    print(ap % 24, bp)
else:    
    print(ap, bp)