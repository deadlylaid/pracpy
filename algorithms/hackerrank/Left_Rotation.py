a, b = input().split()

list_c = list(map(int, input().split()))


for _ in range(0, int(b)):
    a = list_c.pop(0)
    list_c.append(a)

for i in list_c:
    print(i, end=' ')
