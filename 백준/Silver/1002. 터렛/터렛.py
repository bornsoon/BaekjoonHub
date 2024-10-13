import sys
import math

t = [i.strip() for i in sys.stdin.readlines()]
n = int(t[0])

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, t[i+1].split())
    if r1 > r2:
        r1, r2 = r2, r1
    distant = pow(x1 - x2, 2) + pow(y1 - y2, 2) 
    r3 = pow(r1 + r2, 2)
    dr = math.sqrt(distant) + r1
    
    if distant == 0 and r1 == r2:
        print(-1)
    elif distant > r3 or dr < r2:
        print(0)
    elif distant == r3 or dr == r2:
        print(1)
    elif distant < r3:
        print(2)