def solution(date1, date2):
    for i, j in zip(date1, date2):
        if i < j:
            return 1
        elif i > j:
            return 0
    return 0


# 리스트 비교
# def solution(date1, date2):
#     return int(date1 < date2)
