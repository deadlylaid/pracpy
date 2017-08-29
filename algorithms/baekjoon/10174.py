a = int(input())
for _ in range(a):
    b = str(input()).lower()
    b = list(b)
    c = []
    [ c.append(x) for x in b[::-1] ]
    if b == c:
        print('Yes')
    else:
        print('No')
