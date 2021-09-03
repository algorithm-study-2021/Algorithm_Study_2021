a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        if j==a-1:
            print("*")
        else:
            print("*",end='')
