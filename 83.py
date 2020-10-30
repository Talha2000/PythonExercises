# orig_list = [12,24,35,70,88,120,155]
# new_list = [i for (j, i) in enumerate(orig_list) if j not in range(1,4)]
# print(new_list)\

# lst = [12,24,35,70,88,120,155]
# print([i for i in lst if lst.index(i) not in range(2,5)])
lst = [12,24,35,70,88,120,155]

def some(lst):
    new_list = []
    for i in lst:
        if lst.index(i) not in range(2,5):
            new_list.append(i)
    return new_list

print(some(lst))