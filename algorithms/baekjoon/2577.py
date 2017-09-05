num_list = [0,1,2,3,4,5,6,7,8,9]
count_list = [0,0,0,0,0,0,0,0,0,0]
A=int(input())
B=int(input())
C=int(input())
d = str(A*B*C)
e = list(str(d))
for i in e:
    count_list[int(i)] += 1
for i in count_list:
    print(i)
