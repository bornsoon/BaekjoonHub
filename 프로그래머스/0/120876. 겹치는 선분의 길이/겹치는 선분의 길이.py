def solution(lines):
    lines_element = []
    for i in lines:
        lines_element.extend(i)
    lines_max = max(lines_element)
    lines_min = min(lines_element)
    
    arr = [0] * (lines_max - lines_min + 1)
    
    for i in lines:
        for j in range(i[1], i[0], -1):
            arr[j - lines_min] += 1
    
    answer = 0
    for i in arr:
        if i > 1:
            answer += 1
    return answer