a, b = input().split()

c = list(map(int, input().split()))

for i in c:
    if i < int(b):
        print(i, end=' ')
