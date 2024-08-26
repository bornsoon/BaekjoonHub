def solution(arr):
    x = -1
    flag = True
    while flag:
        flag = False
        for i, j in enumerate(arr):
            if j >= 50 and j % 2 == 0:
                arr[i] /= 2
                flag = True
            elif j < 50 and j % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                flag = True
        x += 1
    return x