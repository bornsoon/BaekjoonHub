def solution(score):
    score_sum = [sum(i) for i in score]
    score_sum.sort(reverse=True)
    answer = [score_sum.index(sum(i)) + 1 for i in score]
    return answer