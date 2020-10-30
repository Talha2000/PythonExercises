user_input = tuple(map(int, input().split(',')))

li1 = []
li2 = []

for i in range(0,5):
    li1.append(user_input[i])
print(li1)

for i in range(5,10):
    li2.append(user_input[i])
print(li2)
