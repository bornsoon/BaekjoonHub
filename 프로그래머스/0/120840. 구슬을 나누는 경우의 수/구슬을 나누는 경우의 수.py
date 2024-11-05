def solution(balls, share):
    if balls == share:
        return 1
    if share < balls - share:
        share = balls - share
    answer = balls
    denominator = 1
    n = 1
    for i in range(share+1, balls):
        n += 1
        answer *= i
        denominator *= n
    answer //= denominator
    return answer