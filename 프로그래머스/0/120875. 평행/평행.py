def solution(dots):
    x = dots[3][0]
    y = dots[3][1]
    
    for i in range(3):
        j = (i + 1) % 3
        k = (i + 2) % 3
        d1 = (y - dots[i][1]) / (x - dots[i][0])
        d2 = (dots[j][1] - dots[k][1]) / (dots[j][0] - dots[k][0])
        
        if d1 == d2:
            return 1
    return 0