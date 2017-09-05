A,B=input().split()
C=[x for x in A[::-1]]
D=[x for x in B[::-1]]
a=''.join([str(x) for x in C])
b=''.join([str(x) for x in D])
if int(a) > int(b):
    print(a)
else:
    print(b)
