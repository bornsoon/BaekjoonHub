def solution(sides):
    if sum(sides) > max(sides) * 2:
        return 1
    else:
        return 2