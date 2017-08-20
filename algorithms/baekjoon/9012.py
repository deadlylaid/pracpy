a = int(input())

for i in range(a):
    list_a = list(input())

    stack = []

    index = 0
    while(index<len(list_a)):
        if list_a[index]=='(':
            stack.append('(')
        elif list_a[index]==')':
            if len(stack) == 0:
                stack.append('NO')
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else :
                    stack.append('NO')
                    break
        index+=1
    if len(stack)==0:
        print('YES')
    else:
        print('NO')
