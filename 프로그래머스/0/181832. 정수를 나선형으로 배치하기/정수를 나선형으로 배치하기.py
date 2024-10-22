def solution(n):
    answer = [[0 for i in range(n)] for i in range(n)]
    x = 0
    c = 1
    while(x < n / 2):
        for i in range(x, n - x):
            answer[x][i] = c
            c += 1
        for i in range(x + 1, n - x):
            answer[i][n - x - 1] = c
            c += 1
        for i in range(n - x - 2, x - 1, -1):
            answer[n - x - 1][i] = c
            c += 1
        for i in range(n - x - 2, x, -1):
            answer[i][x] = c
            c += 1

        x += 1   
    return answer