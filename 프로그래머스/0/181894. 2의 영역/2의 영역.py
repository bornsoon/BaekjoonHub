def solution(arr):
    idx1 = -1
    idx2 = idx1
    for i in range(len(arr)):
        if arr[i] == 2:
            idx1 = i
            break
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 2:
            idx2 = i
            break
    if idx1 > -1:
        return arr[idx1:idx2 + 1]
    else:
        return [-1]