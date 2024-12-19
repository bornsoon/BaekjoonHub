def solution(my_string):
    answer = 0
    op = ''
    m = ''
    for i in my_string:
        if i not in ['+', '-']:
            m += i
        else:
            if op == '-':
                answer -= int(m)
            else:
                answer += int(m)
            op = i
            m = ''
            
    if op == '+':
        return answer + int(m)
    else:
        return answer - int(m)

            
            
            