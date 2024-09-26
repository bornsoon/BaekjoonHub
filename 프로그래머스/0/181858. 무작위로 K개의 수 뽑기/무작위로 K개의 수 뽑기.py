def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    if len(answer) != k:
        len_plus = k - len(answer)
        for i in range(len_plus):
            answer.append(-1)
    return answer