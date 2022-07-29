n = int(input())

def fibo(f):
    if f == 0:
        return 0
    elif f == 1 or f == 2:
        return 1
    else:
        return fibo(f-1) + fibo(f-2)

print(fibo(n))
    