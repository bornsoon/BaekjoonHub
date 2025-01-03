def solution(n):
    N = n
    x = 0
    for i in range(2, n):
        while(True):
            if N % i == 0:
                N //= i
                x += 1
            else:
                if x % 2 == 1:
                    return 2
                break
                
    return 1