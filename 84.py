def make3D(a, b, c):
    lst = [ [ [ 0 for col in range(int(c)) ] for col in range(int(b))] for row in range(int(a))]
    return (lst)
a, b, c = input().split(',')

print(make3D(a,b,c))