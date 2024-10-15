def solution(arr, n):
    for i in range(not(len(arr)%2), len(arr), 2):
        arr[i] += n
    return arr