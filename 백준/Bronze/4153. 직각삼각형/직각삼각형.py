import sys

data = sys.stdin.read().splitlines()

for i in data:
    n = list(map(int, i.split()))
    N = max(n)
    if N == 0:
        break
    n.remove(N)
    if N ** 2 == n[0] ** 2 + n[1] ** 2:
        print('right')
    else:
        print('wrong')