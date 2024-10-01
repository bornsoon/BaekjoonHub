N, r, c = map(int, input().split())
count = 0

for i in range(N-1, -1, -1):
    if pow(2, i) <= r:
        if pow(2, i) <= c:
            count += pow(2, i) * pow(2, i) * 3
            r -= pow(2, i)
            c -= pow(2, i)
        else:
            count += pow(2, i) * pow(2, i) * 2
            r -= pow(2, i)
    else:
        if pow(2, i) <= c:
            count += pow(2, i) * pow(2, i) * 1
            c -= pow(2, i)

print(count)