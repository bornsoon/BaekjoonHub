def solution(strArr):
    length = {}
    for i in strArr:
        # if len(i) in length.keys():
        #     length[len(i)] += 1
        # else:
        #     length[len(i)] = 1
    # get함수 사용
        length[len(i)] = length.get(len(i), 0) + 1
    return max(length.values())