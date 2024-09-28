import math

_ = input()
n = list(map(int, input().split()))
if 1 in n:
    n.remove(1)
count = 0

for i in n:
    flag = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        count += 1
print(count)