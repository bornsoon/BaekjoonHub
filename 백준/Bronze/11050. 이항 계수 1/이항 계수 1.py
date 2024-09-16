n, k = map(int, input().split())
def nCk(n ,k):
    N = 1
    if (n - k) < k:
        k = n - k
    for i in range(1, k+1):
        N *= (n-i+1)
        N /= i
    return int(N)
print(nCk(n, k))
        