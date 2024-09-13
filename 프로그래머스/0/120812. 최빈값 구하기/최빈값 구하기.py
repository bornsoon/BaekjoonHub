def solution(array):
    MAX = 0
    answer = ''
    while(array):
        if array.count(array[0]) > MAX:
            MAX = array.count(array[0])
            answer = array[0]
        elif array.count(array[0]) == MAX:
            answer = -1
        array.remove(array[0])
    return answer