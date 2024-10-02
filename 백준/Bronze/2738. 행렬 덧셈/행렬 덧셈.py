import sys

n, m = map(int, input().split())
a = []
b = []

for i in [a,b]:
    for j in range(n):
        _ = list(map(int, sys.stdin.readline().strip().split()))
        i.append(_)

for i, j in zip(a, b):
    _ = m
    for k, l in zip(i, j):
        print(k + l, end=' ')
    m -= 1
    if m:
        print()