def solution(dots):
    x = list(set([i[0] for i in dots]))
    y = list(set([i[1] for i in dots]))
    return abs(x[0] - x[1]) * abs(y[0] - y[1])