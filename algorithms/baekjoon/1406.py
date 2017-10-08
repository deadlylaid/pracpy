f_list=list(input())
count=int(input())
b_list = []
for i in range(count):
    kk = list(input().split())
    if kk[0] == 'L':
        if len(f_list) != 0:
            c = f_list.pop()
            b_list.append(c)
    elif kk[0] == 'D':
            c = b_list.pop(0)
            f_list.append(c)
    elif kk[0] == 'B':
        if len(f_list) != 0:
            f_list.pop()
    elif kk[0] == 'P':
        f_list.append(kk[1])

list_t = f_list+b_list
for i in list_t:
    print(i, end='')
