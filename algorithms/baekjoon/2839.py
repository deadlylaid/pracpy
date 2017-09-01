a = int(input())
divided_by_five = a//5
remainder = a%5

if a>=5:
    while divided_by_five != 0:

        check = a-5*divided_by_five
        if check%3 == 0:
            print(divided_by_five + check//3)
            break
        else:
            divided_by_five -= 1
            if divided_by_five == 0 and a%3 != 0:
                print(-1)
                break
            elif divided_by_five ==0 and a%3 == 0:
                print(a//3)
                break
            elif divided_by_five == 0:
                print(-1)
                break
else:
    if a!=3:
        print(-1)
    else:
        print(1)
