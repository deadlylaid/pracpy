count = int(input())
number_of_star = 2*count-1
for i in range(1, count+1):
    print(' '*(count-i), end='')
    print('*'*(2*i-1))
