x,y = 0, 1

n = int(input("type the limit of the sequence: "))

for i in range(n):
    print(x)
    x, y = y, x + y
