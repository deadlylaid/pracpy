up, down, height = map(int, input().split())
now = 0
min_day = 1
max_day = 1000000000
while min_day<=max_day:
    middle_day = (min_day+max_day)//2
    # 하루가 모두 저물었을 때 = (up*now) - (down * (now-1))
    bb = (up*middle_day) - (down*(middle_day-1))
    if bb==height:
        break
    elif bb>height:
        max_day=middle_day-1
    elif bb<height:
        min_day=middle_day+1
if (up*middle_day) - (down*(middle_day-1)) < height:
    print(middle_day+1)
else:
    print(middle_day)
