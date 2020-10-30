def square(i):
    return i ** 2

lst = [i for i in range(1,21)]
ans = list(map(square, lst))
print(ans)
