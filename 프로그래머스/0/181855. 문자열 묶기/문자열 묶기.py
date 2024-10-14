def solution(strArr):
    length = {}
    for i in strArr:
        if len(i) in length.keys():
            length[len(i)] += 1
        else:
            length[len(i)] = 1
    return max(length.values())