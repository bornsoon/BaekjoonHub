a = int(input())
b = int(input())
c = int(input())

d = list(str(a * b * c))

for i in range(10):
    count = 0
    while True:
        if str(i) in d:
            count += 1
            d.remove(str(i))
        else:
            break
    print(count)