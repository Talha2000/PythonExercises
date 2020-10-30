n = int(input())
sum = 0
def some_func(sum, n):
    for i in range(0, n+1):
        sum+= (i)/(i+1)
    return (round(sum,2))

print(some_func(sum, n))