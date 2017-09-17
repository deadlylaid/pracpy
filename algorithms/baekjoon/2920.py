a=list(map(int, input().split()))
b=sorted(a)
c=sorted(a, reverse=True)
if a==b:
    print('ascending')
elif a==c:
    print('descending')
else:
    print('mixed')
