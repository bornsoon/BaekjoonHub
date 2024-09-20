import copy

a, b = map(int, input().split())
x, y = copy.deepcopy(a), copy.deepcopy(b)

if a < b:
    a, b = b, a
while(b != 0):
    r = a % b
    a, b = b, a
    b = r

print(a)
print(a * (x // a) * (y // a))