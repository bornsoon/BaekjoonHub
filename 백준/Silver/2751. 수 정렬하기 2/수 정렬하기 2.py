import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
n = list(map(int, data[1:]))

n.sort()

for i in n:
    print(i)