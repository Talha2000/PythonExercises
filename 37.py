def some_tuple():
    li = []
    for i in range(1, 21):
        li.append(i ** 2)
    print(tuple(li))

some_tuple()