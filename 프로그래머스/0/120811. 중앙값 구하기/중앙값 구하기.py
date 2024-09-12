def solution(array):
    array.sort()
    if len(array) % 2 == 1:
        return array[len(array)//2]
    else:
        return array[len(array)//2-1]