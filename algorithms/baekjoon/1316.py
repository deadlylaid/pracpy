a=int(input())
count=0
for _ in range(a):
    list_a=list(input())
    check_list=[]
    for i in range(len(list_a)):
        if i==0:
            check_list.append(list_a[i])
        else:
            if list_a[i] in check_list:
                if list_a[i]==list_a[i-1]:
                    pass
                else:
                    check_list.append('False')
                    break
            else:
                check_list.append(list_a[i])
    if 'False' in check_list:
        pass
    else:
        count+=1
print(count)
