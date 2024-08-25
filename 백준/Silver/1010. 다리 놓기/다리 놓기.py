test = int(input())
def mCn(m, n):
    if m == n:
        return 1
        
    if n > (m - n):
        n = m - n 
    for i in range(m - n + 1, m):
        m *= i
    for i in range(1, n):
        n *= i
    return m // n
for i in range(test):
    N, M = map(int, input().split())

    print(mCn(M, N))