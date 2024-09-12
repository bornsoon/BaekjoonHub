def solution(cards):
    point = []
    for i in range(len(cards)):
        point1 = [x for y in point for x in y]
        if cards[i] not in point1:
            temp = []
            j = i
            while(cards[j] not in temp):
                temp.append(cards[j])
                j = cards[j] - 1
            if len(temp):
                point.append(temp)
    score = [len(x) for x in point]
    max1 = max(score)
    score.remove(max1)
    if len(score) != 0:
        max2 = max(score)
    else:
        max2 = 0
    return max1 * max2
            
            