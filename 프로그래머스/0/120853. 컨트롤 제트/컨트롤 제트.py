def solution(s):
    s = s.split(' ')
    num = []
    for i in s:
        if i == 'Z':
            num.pop()
        else:
            num.append(int(i))
    return sum(num)