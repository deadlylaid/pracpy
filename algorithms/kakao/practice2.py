def solution(arr):
    answer = True
    arr.sort()
    for index, i in enumerate(arr):
        if index+1 != i:
            answer = False
            break
        else:
            pass
    return answer
