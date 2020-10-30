n = list(map(int, input().split(',')))

def check(n):
    for i in n:
        try:
            assert i % 2 == 0
            print(str(i) + " is an Even number")
        except AssertionError:
            print(str(i) + " is an odd number")

print(check(n))
