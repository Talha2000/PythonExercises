def gen(n):
    for i in range(0, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

def print_nums(n):
    lst = []
    for i in gen(n):
        lst.append(str(i))
    return (",".join(lst))

n = int(input())

print(print_nums(n))