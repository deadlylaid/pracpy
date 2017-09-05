a=int(input())
b=0
c=1
while a>b:
    b=b+c
    c+=1
for i in range(b-a+1):
    g = c-(i+1)
    h = i+1
if c%2!=0:
    print('{}/{}'.format(str(g), str(h)))
else:
    print('{}/{}'.format(str(h), str(g)))
