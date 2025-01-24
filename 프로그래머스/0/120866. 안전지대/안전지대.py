def solution(board):
    n, m = len(board[0]), len(board)
    answer = n * m
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    for i in range(n):
        for j in range(m):
            flag = False
            for k in range(8):
                if board[j][i] == 1:
                    answer -= 1
                    break
                x = j + dx[k]
                y = i + dy[k]
                if x >= 0 and y >= 0 and x < m and y < n:
                    if board[x][y] == 1:
                        answer -= 1
                        break
                
                
    return answer