def solution(my_string):
    alpha_dict = {}
    answer = []
    for i in range(65, 91):
        alpha_dict[chr(i)] = 0
    for i in range(97, 123):
        alpha_dict[chr(i)] = 0 
    for i in my_string:
        alpha_dict[i] += 1
    for i in range(65, 91):
        answer.append(alpha_dict[chr(i)])
    for i in range(97, 123):
        answer.append(alpha_dict[chr(i)])
    return answer