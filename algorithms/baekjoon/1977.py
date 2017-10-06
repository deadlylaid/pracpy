list_a=list(map(lambda x:x*x, [ x for x in range(1,101)]))

a=int(input())
b=int(input())

result = []
sum0=0
for i in list_a:
    if i>=a and i<=b:
        result.append(i)
    else:
        pass

if len(result) == 0:
    print(-1)
else:
    for i in result:
        sum0+=i
    print(sum0)
    print(min(result))
