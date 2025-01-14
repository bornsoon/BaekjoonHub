def solution(keyinput, board):
    answer = [0, 0]
    dir = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    x = (board[0] - 1) // 2
    y = (board[1] - 1) // 2
    for i in keyinput:
        dx = answer[0] + dir[i][0]
        dy = answer[1] + dir[i][1]
        if dx <= x and dx >= x * (-1):
            answer[0] = dx
        if dy <= y and dy >= y * (-1):
            answer[1] = dy
    return answer