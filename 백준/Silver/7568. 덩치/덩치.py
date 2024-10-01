import sys

n = int(input())
_ = [list(map(int, i.split())) for i in sys.stdin.readlines()]
answer = []

for i in _:
    rank = 1
    for j in _:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    answer.append(str(rank))

print(' '.join(answer))