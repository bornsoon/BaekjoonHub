def solution(myString, pat):
    answer = [-1]
    for i in range(len(myString)):
        n = myString.find(pat,i)
        if n not in answer:
            answer.append(n)
    return len(answer) - 1

# return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))
# answer = 0
#    for i, x in enumerate(myString) :
#        if myString[i:].startswith(pat) :
#            answer += 1
#    return answer
