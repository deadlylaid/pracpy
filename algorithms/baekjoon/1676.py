n=[ x for x in range(1, int(input())+1) ]
x=1
for i in n:
    x*=i

zero=0
for i in list(str(x))[::-1]:
    if i == '0':
        zero+=1
    else:
        break
print(zero)
