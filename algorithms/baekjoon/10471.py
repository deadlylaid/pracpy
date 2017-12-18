num_list = [0]
width,count = map(int, input().split())
for i in map(int, input().split()):
    num_list.append(i)
num_list.append(width)

count_list = []

for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
        if num_list[j] - num_list[i] in count_list:
            pass
        else:
            count_list.append(num_list[j]-num_list[i])

count_list.sort()

for i in count_list:
    print(i, end=' ')
