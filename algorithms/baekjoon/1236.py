a,b = map(int, input().split())

castle=[]
x = [False] * a
y = [False] * b

for i in range(a):
    castle.append(list(input()))

for i in range(a):
    for j in range(b):
        if castle[i][j] == 'X':
            x[i] = True
            y[j] = True

count_x=0
count_y=0
for i in x:
    if i is False:
        count_x+=1

for i in y:
    if i is False:
        count_y+=1

print(max(count_x, count_y))
