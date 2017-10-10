# 거리 1 2 / 3 4 / 5 6 / 7 8 9 / 10 11 12 / 13 14...
# 최소 1 2 / 3 3 / 4 4 / 5 5 5 / 6 6 6 /...
count = int(input())
for _ in range(count):
    a,b=map(int, input().split())
    length=b-a
    selected_num=0
    while True:
        selected_num+=1
        if selected_num**2 >= length:
            break
    if (selected_num**2)-(selected_num-1) > length:
        print(selected_num*2-2)
    else:
        print(selected_num*2-1)
