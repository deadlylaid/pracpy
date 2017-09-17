a=int(input())
b=list(map(int, input().split()))
c=int(input())

b.sort()

max_int = b[-1]
min_int = b[0]

if c<min_int:
    max_int=min_int
    min_int=0

else:
    for index, i in enumerate(b):
        if c-i==0:
            max_int=0
            min_int=0
            break
        elif c-i<0:
            max_int=b[index]
            min_int=b[index-1]
            break

count=0
for i in range(min_int+1, max_int):
    for j in range(min_int+1, max_int):
        if i<j and i<=c and j>=c:
            count+=1

print(count)
