import sys

n = int(input())

if n == 0:
    print(0)
else:
    answer = [int(i) for i in sys.stdin.readlines()]
    answer.sort()

    s = int(len(answer)*0.15 + 0.5)
    idx = len(answer) - s


    print(int(sum(answer[s:idx])/(len(answer) -2*s) + 0.5))
