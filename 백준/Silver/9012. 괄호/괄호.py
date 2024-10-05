import sys

n = int(input())
for i in range(n):
    ps = sys.stdin.readline().strip()
    count = 0
    for j in ps:
        if j == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print('NO')
            break
    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')