def solution(num_list):
    l = len([i for i in num_list if i%2==0])
    return [l, len(num_list) - l ]