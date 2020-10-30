n = int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def print_list(n):
    lst = []
    for i in range(0, n+1):
        lst.append(str(fib(i)))
    return (",".join(lst))

print(print_list(n))

