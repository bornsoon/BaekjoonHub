import sys

b = 0
N = int(input())

for _ in range(N):
    x = sys.stdin.readline().split()
    if len(x) == 1:
        if x[0] == 'all': 
            b = (1 << 21) - 2
        elif x[0] == 'empty':
            b = 0
    else:
        n = int(x[1])

        if x[0] == 'add':
            b |= (1 << n)
        elif x[0] == 'remove':
            b &= ~(1 << n)
        elif x[0] == 'check':
            if b & (1 << n) > 0:
                print(1)
            else:
                print(0)
        elif x[0] == 'toggle':
            b ^= (1 << n)