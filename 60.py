n = int(input())

def fib(n):
    if n == 0:
        return 0
    return fib(n-1)+100

print(fib(n))
