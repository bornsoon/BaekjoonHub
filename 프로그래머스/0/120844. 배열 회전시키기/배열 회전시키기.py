def solution(numbers, direction):
    if direction == "right":
        answer = [numbers.pop()]
        answer += numbers
    else:
        temp = [numbers.pop(0)]
        answer = numbers + temp
    return answer