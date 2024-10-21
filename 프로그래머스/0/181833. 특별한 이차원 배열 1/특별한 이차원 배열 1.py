def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(int(i == j))
        answer.append(temp)
    return answer