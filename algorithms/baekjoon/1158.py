a, b = int(input().split())

c = [ int(x) for i in range(1, a+1) ]
d = []

index = b-1

while(len(c) != 0):

    c.pop(index)
    index += b
    if index > len(c)-1
