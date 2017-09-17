def solve(i):
    a=list(str(i))
    b=len(a)
    c=i
    for j in a:
        c+=int(j)
    return c

fuck=[]

for i in range(1, 10001):
    k = solve(i)
    if k<10001:
        fuck.append(k)
for i in range(1, 10001):
    if i not in fuck:
        print(i)
