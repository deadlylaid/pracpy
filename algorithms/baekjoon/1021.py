a,b=map(int,input().split())
c = list(map(int,input().split()))
tt = []
list_a=[x for x in range(1,a+1)]

result = 0
def check(value, i, list_a):
    for j in list_a:
        if j == i:
            return value
        else:
            value+=1

for i in c:
    while True:
        value = 0
        if i == list_a[0]:
            list_a.pop(0)
            break
        else:
            value = check(value, i, list_a)
            last_index = len(list_a)
            if value >= last_index - value:
                tt = list_a[value:]
                del(list_a[value:])
                list_a = tt + list_a
                result+=(last_index-value)
            else:
                tt = list_a[:value]
                del(list_a[:value])
                list_a = list_a + tt
                result+=value

print(result)
