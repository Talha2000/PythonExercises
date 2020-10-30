
def RemoveEven(user):
    lst = []
    for i in user:
        if i % 2 != 0:
            lst.append(i)
    return lst
            

user = list(map(int,input().split(',')))

print(RemoveEven(user))