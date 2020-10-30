user_input = tuple(map(int, input().split(',')))

lst_even = []
lst_odd = []
for i in range(len(user_input)):
    if i % 2 == 0:
        lst_even.append(i)
    lst_odd.append(i)
print(lst_even)