def solution(my_string):
    answer = 0
    num = ''
    for n in my_string:
        if n.isdigit():
            num += n
        else:
            if num:
                answer += int(num)
                num = ''
    if num:
            answer += int(num)
    return answer