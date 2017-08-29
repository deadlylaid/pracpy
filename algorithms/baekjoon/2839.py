a = int(input())
b = int(a/5)
c = a%5
if c == 0:
    print(b)
else:
    d = int(c/3)
    e = int(d%3)
    print(e)
    if e == 0:
        print(int(b+d))
    elif e != 0:
        print(-1)

