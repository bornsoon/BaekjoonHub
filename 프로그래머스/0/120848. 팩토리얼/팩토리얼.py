def solution(n):
    i = 1
    answer = 1
    while(True):
        if answer <= n:
            i += 1
            answer *= i
        else:
            return i - 1