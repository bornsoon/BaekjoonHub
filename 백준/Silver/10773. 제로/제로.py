n = int(input())
num = []

for i in range(n):
    m = int(input())
    if m != 0:
        num.append(m)
    else:
        if num:
            num.pop()

print(sum(num))