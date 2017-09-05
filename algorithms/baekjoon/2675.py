for i in range(int(input())):
    A,B=input().split()
    list_a = list(B)
    d=''
    for i in list_a:
        d+=i*int(A)
    print(d)
