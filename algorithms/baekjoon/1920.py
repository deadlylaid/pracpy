def solve(A, B, C, D):

    left = A
    right = B

    my_list = C
    my_num = D

    middle = (left+right)//2

    if middle == 0:
        if my_num == my_list[middle] or my_num == my_list[middle+1]:
            print(1)
        else:
            print(0)
    elif left > right:
        print(0)

    else:
        if my_num == my_list[middle]:
            print(1)
        elif my_num > my_list[middle]:
            left = middle+1
            solve(left,right, my_list, my_num)
        elif my_num < my_list[middle]:
            right = middle-1
            solve(left,right, my_list, my_num)

first_input = int(input())
first_list = [int(x) for x in input().split()]
first_list.sort()

second_input = int(input())
second_list = [int(x) for x in input().split()]

for i in second_list:
    solve(0, first_input-1, first_list, i)
