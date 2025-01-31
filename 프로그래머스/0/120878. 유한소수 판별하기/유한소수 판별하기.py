def solution(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a 

    c = gcd(a, b)
    
    b //= c
    
    while b % 2 == 0:
            b //= 2
    while True:
        if b % 5 == 0:
            b //= 5
        else:
            break
            
    if b == 1:
        return 1
    else:
        return 2