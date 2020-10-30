from random import shuffle

user = list(map(int, input().split(',')))

shuffle(user)
print(user)