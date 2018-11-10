a = int(input())

def hansoo(a):
    if a < 100:
        return a
    else:
        bb = 99
        for i in range(100, a+1):
            list_a = list(str(i))
            der = int(list_a[0])-int(list_a[1])
            for i in range(len(list_a)-1):
                if int(list_a[i]) - int(list_a[i+1]) != der:
                    bb-=1
                    break
            bb+=1
    return bb

print(hansoo(a))
