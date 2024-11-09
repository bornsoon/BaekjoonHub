def solution(numbers, direction):
    if direction == "right":
        answer = [numbers.pop()]
        answer += numbers
    else:
        answer = numbers + [numbers.pop(0)]
    return answer