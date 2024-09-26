import math

n = int(input())
t = 0
m = list(map(int, input().split()))
T, P = map(int, input().split())
for i in m:
    j = math.ceil(i / T)
    t += j
p1 = n // P
p2 = n % P

print(t)
print(p1, p2)