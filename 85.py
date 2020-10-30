user_input = list(input().split(','))

def remove_index(user_input):
    lst = []
    for i, j in enumerate(user_input):
        if i != 0 and i != 4 and i != 5:
            lst.append(j)
    return ','.join(lst)

print(remove_index(user_input))