def solution(quiz):
    answer = []
    for i in quiz:
        x, op, y, _, z = i.split(" ")
        
        if op == "-":
            if int(x) - int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(x) + int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
            
    return answer