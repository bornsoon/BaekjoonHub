def solution(spell, dic):
    flag = False
    for i in dic:
        temp = [i.count(x) for x in spell]
        cnt = 1
        for j in temp:
            cnt *= j
        if cnt == 1:
            flag = True
    return 1 if flag else 2