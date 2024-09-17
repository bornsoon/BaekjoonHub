import sys

data = sys.stdin.readlines()
N = int(data[0])
answer = []
for i in range(N):
    answer.append(list(map(int, data[i+1].split())))
answer.sort(key=lambda x: (x[0], x[1]))
for i in answer:
    print(i[0], i[1])