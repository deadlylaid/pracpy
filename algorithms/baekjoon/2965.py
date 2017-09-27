a,b,c = map(int,input().split())
c-=b
b-=a
print(max(c,b)-1)
