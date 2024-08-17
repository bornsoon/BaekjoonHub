def solution(num_list):
    return next((num_list.index(i) for i in num_list if i < 0), -1)