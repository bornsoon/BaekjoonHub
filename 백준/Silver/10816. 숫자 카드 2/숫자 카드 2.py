input()
nc = list(map(int, input().split()))
input()
mc = list(map(int, input().split()))

dict = {}

for i in mc:
    dict[i] = 0

for i in nc:
    if i in dict:
        dict[i] += 1
    
for i in mc:
    print(dict[i], end=' ')