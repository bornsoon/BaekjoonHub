def solution(s):
    char = {}
    for i in s:
        if s.count(i)  == 1:
            char[ord(i)] = i
    answer = ''
    for i in sorted(char.keys()):
        answer += char[i]
    return answer