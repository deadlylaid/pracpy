import math
count = int(input())

result = []
a = []

for i in range(1, count+1):
    a = list(map(int, input().split()))
    x1 = a[0]
    y1 = a[1]
    r1 = a[2]
    x2 = a[3]
    y2 = a[4]
    r2 = a[5]
    x3 = x2-x1
    y3 = y2-y1
    r3 = r2+r1
    b = math.sqrt((x3*x3)+(y3*y3))

    # 좌표값이 같을 때
    if x1 == x2 and y1 == y2:
        if r2 == r1:
            result.append(-1)
        else:
            result.append(0)
    # 반지름의 합과 두 점 사이의 거리가 같을 때
    elif r3 == b:
        result.append(1)
    # 반지름의 합보다 두 점 사이의 거리가 더 길 때
    elif r3 < b:
        result.append(0)
    elif r3 > b:
        if b+r1 < r2 or b+r2 < r1:
            result.append(0)
        elif b+r1 == r2 or b+r2 == r1:
            result.append(1)
        elif b+r1 > r2 or b+r2 > r1:
            result.append(2)

for i in result:
    print(i)
