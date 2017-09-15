def solution(n):
    a=list(str(n))
    answer = 0
    for i in a:
        answer+=int(i)
    return answer
