def solution(arr):
    a, b = len(arr), len(arr[0])
    
    if a > b:
        n = a - b
        for i in range(a):
            arr[i].extend([0] * n)
    elif b > a:
        n = b - a
        for i in range(n):
            arr.append([0] * b)
    return arr