def solution(arr):
    l = len(arr)
    num = 1
    while (l > num):
        num *= 2
    arr0 = [0 for i in range(num-l)]
    return arr + arr0