a = int(input())

b = []

c = []

for _ in range(0, a):
    b.append(list(map(int, input().split())))

for i in range(0, len(b)):
    if b[i][0] == 1:
        c.append(b[i][1])
    elif b[i][0] == 2:
        c.pop()
    elif b[i][0] == 3:
        print(max(c))
