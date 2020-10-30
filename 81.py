
user = list(map(int, input().split(',')))

lst = [i for i in user if i % 5 != 0 and i % 7 != 0]
print(lst)