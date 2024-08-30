stick = [64]
X = int(input())
while sum(stick) > X:
    for i in range(len(stick)):
        if stick[i] == min(stick):
            stick[i] /= 2
            break
    if sum(stick) >= X:
        continue
    else:
        stick.append(min(stick))
print(len(stick))