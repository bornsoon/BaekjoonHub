def solution(arr):
    x = 0
    while(True):
        count = 0
        for i, j in enumerate(arr):
            if j >= 50 and j % 2 == 0:
                arr[i] /= 2
            elif j < 50 and j % 2 == 1:
                arr[i] = arr[i] * 2 + 1
            if (j < 50 and j % 2 == 0) or (j >= 50 and j % 2 == 1):
                count += 1
            else:
                pass
        if count == len(arr):
            break
        x += 1
    return x