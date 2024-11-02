def solution(hp):
    l = hp // 5
    m = (hp - l * 5) // 3
    n = hp - l * 5 - m * 3
    return l + m + n