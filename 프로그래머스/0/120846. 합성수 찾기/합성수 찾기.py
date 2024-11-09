def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(2, n+1):
            if i % j == 0:
                if i != j:
                    answer += 1
                    break
                else:
                    break
    return answer