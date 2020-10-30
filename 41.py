def square(i):
    return i ** 2

lst = [i for i in range(1,11)]
print(list(map(square, lst)))