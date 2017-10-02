a=input()
b=1
for i in a:
    if b%10==0:
        print(i)
    else:
        print(i, end='')
    b+=1
