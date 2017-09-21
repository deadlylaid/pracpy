brackets = list(input())
stack = []
closed = [')', ']' ]
opened = ['(', '[' ]
result = 0
num = 0

def cal_stack(stack, bracket):

    pre_value = 1
    for i in stack[::-1]:
        if type(i) == int:
            if pre_value == 1:
                pre_value = i
                stack.pop()
            else:
                stack.pop()
                pre_value+=i
        else:
            # 여기 들어왔을 때 괄호안의 숫자는 무조건 1개가 되도록 만들어야함
            if i == '(' and bracket == ')':
                pre_value*=2
                stack.pop()
                stack.append(pre_value)
                break
            elif i == '[' and bracket == ']':
                pre_value*=3
                stack.pop()
                stack.append(pre_value)
                break
    return stack

for i in brackets:
    if i in opened:
        stack.append(i)
    elif i in closed:
        if len(stack) is 0:
            result = 0
            break
        else:
            b = stack[-1]
            if b not in opened:
                stack = cal_stack(stack, i)
                if stack == -1:
                    result=0
                    break
            else:
                if i == ')' and b == '(':
                    stack.pop()
                    stack.append(2)
                elif i == ']' and b == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    result = 0
                    break
for i in stack:
    if type(i) is str:
        result=0
        break
    else:
        result += i

print(result)
