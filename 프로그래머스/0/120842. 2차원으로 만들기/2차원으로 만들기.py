def solution(num_list, n):
    answer = []
    temp = []
    j = 1
    for i in num_list:
        temp.append(i)
        if j == n:
            j = 0
            answer.append(temp)
            temp = []
        j += 1
        
    return answer