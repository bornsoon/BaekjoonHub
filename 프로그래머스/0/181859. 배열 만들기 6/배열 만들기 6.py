def solution(arr):
    answer = []
    i = 0
    for i in arr:
        if answer:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
        else:
              answer.append(i)  
    return answer if answer else [-1]