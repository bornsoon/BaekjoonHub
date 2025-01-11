def solution(array, height):
    return len([1 for i in array if i > height])