a=list(input().upper())
a.sort()
zz = a[0]
count = 0
list_a = [0]
max_str = 0
fuck=0
for i in a:
    if zz == i:
        count+=1
        max_str=i
    else:
        if max(list_a) == count:
            fuck=1
        else:
            list_a.append(count)
            count=0
            fuck=0
if fuck==0:
    print(max_str)
else:
    print('?')

