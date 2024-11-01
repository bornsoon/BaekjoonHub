def solution(n):
    if n == 1:
        return 1
    answer = []
    for i in range(1, n):
        if n % i == 0:
            if (n//i, i) in answer:
                break
            else:
                answer.append((i, n//i))
    
    if answer[-1][0] == answer[-1][1]:
        return 2 * len(answer) -1
    else:        
        return 2 * len(answer)