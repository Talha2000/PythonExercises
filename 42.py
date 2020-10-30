def even(i):
    return i % 2 == 0

def square(i):
    return i ** 2

lst = [i for i in range(1,11)]
lst = map(square, filter(even, lst))
print(list(lst))