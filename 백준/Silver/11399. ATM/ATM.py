n = int(input())
p = list(map(int, input().split()))

p.sort()
sum = 0

for i in range(n):
    sum += (n-i) * p[i]

print(sum)