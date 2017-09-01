def solve(first_value, a, b, count):
    count += 1
    front_num = int(a)
    back_num = int(b)

    check_num = str(front_num) + str(back_num)

    sum_num = front_num + back_num
    list_sum = list(str(sum_num))

    check_num = str(back_num) + str(list_sum[-1])
    if int(first_value) == int(check_num):
        print(count)
    else:
        solve(first_value, back_num, list_sum[-1], count)

first_value = input()
value_list = list(first_value)

if len(value_list) == 1:
     solve(first_value, 0, value_list[-1], 0)
else:
     solve(first_value, value_list[0], value_list[1], 0)
