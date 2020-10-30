num = int(input("Enter a number"))



def some_func(sum, num):
    for i in range(1, num + 1):
        sum += i/(i+1)
    return (round(sum,2))

print(some_func(0, num))