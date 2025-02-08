def solution(babbling):
    pron = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in pron:
            if i.strip():
                i = i.replace(j, ' ')
            else:
                break
        if i.strip():
            if i in pron:
                answer += 1  
        else:
            answer += 1 
    return answer