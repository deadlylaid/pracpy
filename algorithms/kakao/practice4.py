def check(value, index_x, index_y, board):

    if index_x == 0:
        return value
    if index_y == 0:
        return value
    if value == 0:
        return value

    new_x = board[index_x][index_y-1]
    new_y = board[index_x-1][index_y]
    new_xy = board[index_x-1][index_y-1]

    if (new_x * new_y * new_xy) == 0:
        result = 1
    else:
        result = min(new_x, new_y, new_xy) + 1
    return result

def solution(board):

    board_len = len(board)

    for i in range(board_len):
        for j in range(len(board[i])):
            board[i][j] = check(board[i][j], i, j, board)
    answer = max([ max(sub) for sub in board ])

    return answer*answer
