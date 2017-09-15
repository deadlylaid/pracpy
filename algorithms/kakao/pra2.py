def solution(arr):
    answer = True
    set_a = set(arr)
    if len(set_a)!=len(arr):
        print('false')
    else:
        if len(arr)!=max(arr):
            print('false')
        else:
            print('true')
    return answer

a=input()
solution(a)
