import sys 

N = int(input())
s = '0' * 10000
s = list(s)
for i in range(N):
    n = int(sys.stdin.readline())
    s[n - 1] = str(int(s[n - 1]) + 1)

for i, j in enumerate(s):
    if j != '0':
        for k in range(int(j)):
            print(i + 1)