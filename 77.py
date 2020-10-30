import time

a = time.time()
for i in range(0, 100001):
    x = 1+1

b = time.time()
result = b - a
print(result)