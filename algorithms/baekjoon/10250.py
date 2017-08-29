a = int(input())

for i in range(a):

    H, W, person = input().split()

    st = int(person)%int(H)
    ho = int(person)//int(H) + 1
    if person==0:
        st=1
        ho -= 1
    elif st==0:
        st=H
        ho -= 1
    tt = list(str(ho))
    # 호수가 10의 자리면
    if len(tt)>1:
        print(str(st)+str(ho))
    else:
        print("{}0{}".format(str(st), str(ho)))
