a,b=map(int, input().split())
c=[]
d=[]
for i in range(a):
    c.append([0]*b)
    d.append(list(map(int,input().split())))

def check(dp, a, b, value):

    if a == 0 and b == 0:
        return value
    elif a == 0:
        return c[a][b-1] + value
    elif b == 0:
        return c[a-1][b] + value
    else:
        return max(c[a-1][b]+value, c[a][b-1]+value, c[a-1][b-1]+value)

for i in range(a):
    for j in range(b):
        c[i][j] = check(c, i, j, d[i][j])

print(c[a-1][b-1])
