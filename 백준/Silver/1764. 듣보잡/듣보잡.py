import sys

n, m = map(int, input().split())

t = sys.stdin.readlines()

if n > m:
    num = n
    set1 = set(t[:n])
    set2 = set(t[n:])
else:
    num = m
    set1 = set(t[n:])
    set2= set(t[:n])

count = 0
answer = set()
for i in set1:
    if i in set2:
        count +=1
        answer.add(i.strip())

print(count)
for i in sorted(answer):
    print(i)