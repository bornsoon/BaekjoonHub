def solution(num_list):
    return next((i for i, j in enumerate(num_list) if j < 0), -1)