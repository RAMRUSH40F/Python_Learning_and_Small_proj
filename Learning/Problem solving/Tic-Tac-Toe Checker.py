def winning_streak(array):
    if 0 not in array:
        # print(array)
        div = (array[0] + array[1] + array[2])/3
        return div

def is_solved(board):

    #Check rows
    for row in board:
        div = winning_streak(row)
        if div in [ 1, 2 ]:
            return int(div)

    #Check columns and diag
    for i in range(3):
        div = winning_streak([board[0][i], board[1][i], board[2][i]])
        if div in [1,2] :
            return int(div)

    #Check diagonals

    div = winning_streak([ board[ 0 ][ 0 ], board[ 1 ][ 1 ], board[ 2 ][ 2 ] ])
    if div in [ 1, 2 ]:
        return int(div)

    winning_streak([ board[ 0 ][ 2 ], board[ 1 ][ 1 ], board[ 2 ][ 0 ] ])
    if div in [ 1, 2 ]:
        return int(div)

    #Check if there are some free space left
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return -1
    return 0


# print(is_solved([[1,2,1],[1,1,2],[2,1,2]]))




