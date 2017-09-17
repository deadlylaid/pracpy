a=int(input())
for i in range(a):
    b=list(input())

    c=[]
    count=0
    for i in b:
        if i =='O':
            count+=1
            c.append(count)
        elif i == 'X':
            count=0
    d=0
    for i in c:
        d+=i
    print(d)
