def solution(n):
    num = 0
    i = 1
    cnt = 1
    while cnt < n:
        i += 1
        if i % 3 == 0 or '3' in str(i):
            num += 1
        else:
            cnt += 1
    return n + num