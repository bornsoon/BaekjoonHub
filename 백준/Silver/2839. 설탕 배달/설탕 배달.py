n = int(input())

flag = False

for i in range(n // 5, -1, -1):
    min = i
    if (n - i * 5) % 3 != 0:
        continue
    else:
        min +=  (n - i * 5) // 3
        flag = True
        break

if flag:
    print(min)
else:
    print(-1)