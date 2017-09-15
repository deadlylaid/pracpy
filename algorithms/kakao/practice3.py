def solution(v):
    answer = []
    list_x=[]
    list_y=[]
    for i in range(3):
        list_x.append(v[i][0])
        list_y.append(v[i][1])
    list_x.sort()
    list_y.sort()
    if list_x[1] == list_x[0]:
        answer.append(list_x[2])
    else:
        answer.append(list_x[0])
    if list_y[1] == list_y[0]:
        answer.append(list_y[2])
    else:
        answer.append(list_y[0])
    return answer
