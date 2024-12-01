def solution(my_string):
    answer = ''
    my_set = set()
    
    for i in my_string:
        if i not in my_set:
            my_set.add(i)
            answer += i           
        
    return answer