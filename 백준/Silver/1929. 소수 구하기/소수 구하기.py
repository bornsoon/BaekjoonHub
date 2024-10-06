n, m = map(int, input().split())

if n == 1:
    n = 2

num = set([])

for i in range(n, m + 1):
    num.add(i)
    
for i in range(2, m + 1):
    j = m // i
    for k in range(2, j + 1):
        num.discard(i * k)
num = list(num)
num.sort()
                
for i in num:
    print(i)