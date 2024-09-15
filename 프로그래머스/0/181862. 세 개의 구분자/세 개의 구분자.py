def solution(myStr):
    answer = []
    myStr = myStr.strip()
    myStr = myStr.replace('b', 'a')
    myStr = myStr.replace('c', 'a')
    myStr = myStr.split('a')
    for i in myStr:
        if i != "":
            answer.append(i)
    return answer if answer else ["EMPTY"]