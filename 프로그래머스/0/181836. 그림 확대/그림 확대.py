def solution(picture, k):
    answer = []
    for i in picture:
        str = ''
        for l in i:
            str += l * k
        for h in range(k):
            answer.append(str)
    return answer