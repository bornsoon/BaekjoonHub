def solution(array, n):
    arr = [i - n if i > n else n - i for i in array]
    answer = []
    for i in array:
        if i > n:
            if i - n == min(arr):
                answer.append(i)
        else:
            if n - i == min(arr):
                answer.append(i)
    return min(answer)