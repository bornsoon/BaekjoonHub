def solution(n):
    answer = []
    for i in range(2, n):
        if n % i == 0:
            n /= i
            answer.append(i)
            while(True):
                if n % i == 0:
                    n /= i
                else:
                    break
    if not answer:
        answer = [n]
    return answer