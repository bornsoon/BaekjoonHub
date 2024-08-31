def solution(myString, pat):
    answer = [-1]
    for i in range(len(myString)):
        n = myString.find(pat,i)
        if n not in answer:
            answer.append(n)
    return len(answer) - 1