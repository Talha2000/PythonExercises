user_input = list(input().split(','))

def remove_24(user_input):
    lst = []
    for i in user_input:
        if i != '24':
            lst.append(i)
    return ','.join(lst)

print(remove_24(user_input))