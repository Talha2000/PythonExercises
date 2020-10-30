def even(i):
    return i % 2 == 0 

lst = [i for i in range(1,21)]
print(list(filter(even, lst)))