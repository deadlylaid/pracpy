a=int(input())
a_list=list(map(int, input().split()))

b=int(input())
b_list=list(map(int, input().split()))

a_list.sort()

result_list = []
for index, i in enumerate(b_list):
    first_index = 0
    last_index = a-1

    while first_index<=last_index:
        middle_index = (first_index + last_index)//2
        if i == a_list[middle_index]:
            result_list.append(1)
            break
        elif i > a_list[middle_index]:
            first_index = middle_index+1
        elif i < a_list[middle_index]:
            last_index=middle_index-1
    if len(result_list) <= index:
        result_list.append(0)

for i in result_list:
    print(i, end=' ')
