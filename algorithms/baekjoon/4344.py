a = int(input())

for _ in range(a):
    list_b = list(map(int, input().split()))
    c = list_b[0]
    d = 0
    for i in range(1, c+1):
        d += list_b[i]

    average = d/c
    f = 0
    for i in list_b[1:]:
        if i > average:
            f+=1
    result_value = '{:0.3f}'.format(f/c*100) + '%'

    print(result_value)
