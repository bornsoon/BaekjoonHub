def solution(myString, pat):
    myString = myString.replace('A', 'a').replace('B', 'A').replace('a', 'B')
    return 1 if pat in myString else 0