def solution(n):
    answer = []
    for i in range(2, n):
        if n % i == 0:
            flag = True
            for j in answer:
                if i % j == 0:
                    flag = False
                    break
            if flag:
                answer.append(i)
    if not answer:
        answer = [n]
    return answer