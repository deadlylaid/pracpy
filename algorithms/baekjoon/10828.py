a = int(input())

c = []
for i in range(a):
    b = (input().split())
    if b[0] == 'push':
        c.append(b[1])
    elif b[0] == 'pop':
        if len(c)==0:
            print(-1)
        else:
            print(c.pop())
    elif b[0] == 'size':
        print(len(c))
    elif b[0] == 'empty':
        if len(c) == 0:
            print(1)
        else:
            print(0)
    elif b[0] =='top':
        if len(c) == 0:
            print(-1)
        else:
            print(c[-1])
