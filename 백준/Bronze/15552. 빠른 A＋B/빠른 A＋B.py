import sys

N = int(input())
num = []
for i in range(N):
    _ = map(int, sys.stdin.readline().rstrip().split())
    num.append(_)

for i in num:
    print(sum(i))