def check(value, index_x, index_y, board):

    if index_x == 0:
        return value
    elif index_y == 0:
        return value
    elif value == 0:
        return value
    else:
        new_x = board[index_x-1][index_y]
        new_y = board[index_x][index_y-1]
        new_xy = board[index_x-1][index_y-1]
    if (new_x * new_y * new_xy) == 0:
        return 1
    else:
        return min(new_x, new_y, new_xy) + 1

def solution(board):

    board_len = len(board)

    for i in range(board_len):
        for j in range(4):
            board[i][j] = check(board[i][j], i, j, board)
#    answer = max([ max(sub) for sub in board ]) ** 2
    answer = board

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
