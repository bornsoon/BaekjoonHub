X = int(input())

num = [0] * (X + 1)

for i in range(2, X + 1):
    if i % 6 == 0 and num[i // 2] < num[i // 3] and num[i // 2] < num[i - 1]:
        num[i] = num[i // 2] + 1
    elif i % 3 == 0 and num[i // 3] < num[i - 1]:
        num[i] = num[i // 3] + 1
    elif i % 2 == 0 and num[i // 2] < num[i - 1]:
        num[i] = num[i // 2] + 1
    else:
        num[i] = num[i - 1] + 1
        
print(num[X])