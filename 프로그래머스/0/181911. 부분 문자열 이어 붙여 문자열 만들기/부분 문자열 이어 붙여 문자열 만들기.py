def solution(my_strings, parts):
    return ''.join(my_strings[i][j:k + 1] for i, (j, k) in enumerate(parts))