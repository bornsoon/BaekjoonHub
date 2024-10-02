import sys

n = [i for i in range(1, 31)]

for i in range(28):
    _ = int(sys.stdin.readline().rstrip())
    n.remove(_)

n.sort()
for i in n:
    print(i)