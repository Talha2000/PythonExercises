
user = list(map(int, input().split(',')))

lst = [user[i] for i in range(len(user)) if i % 2 != 0]

print(lst)
