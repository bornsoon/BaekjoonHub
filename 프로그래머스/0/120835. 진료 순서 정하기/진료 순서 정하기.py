def solution(emergency):
    dict = {}
    answer = []
    for idx, i in enumerate(sorted(emergency, reverse=True)):
        dict[i] = idx + 1
    for i in emergency:
        answer.append(dict[i])
    return answer