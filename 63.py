def evenGenerator(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

def print_list(n):
    lst = []
    for i in evenGenerator(n):
        lst.append(str(i))
    return (",".join(lst))

n = int(input())

print(print_list(n))