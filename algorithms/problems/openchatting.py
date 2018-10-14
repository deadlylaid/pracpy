def solution(record):
    answer = []
    userid_nickname = {}
    for line in record:
        splited_line = line.split(' ')
        if len(splited_line) == 3:
            userid_nickname.update({splited_line[1]:splited_line[-1]})

    for line in record:
        splited_line = line.split(' ')
        if len(splited_line) == 3:
            if splited_line[0] == "Enter":
                answer.append(userid_nickname[splited_line[1]]+"님이 들어왔습니다.")
        else:
            answer.append(userid_nickname[splited_line[1]]+"님이 나갔습니다.")
    return answer
