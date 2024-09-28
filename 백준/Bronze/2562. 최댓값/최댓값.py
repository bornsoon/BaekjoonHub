import sys
n = list(map(int, sys.stdin.read().split()))
m = max(n)
print(m)
print(n.index(m) + 1)