import sys

N, M = map(int, input().split())
data = sys.stdin.read().split()
pokemon = {}

for i in range(N):
    pokemon[data[i]] = i


for i in range(N, N+M):
    if data[i].isdigit():
        print(data[int(data[i])-1])
    else:
        print(pokemon[data[i]]+1)