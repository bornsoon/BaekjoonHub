def solution(numer1, denom1, numer2, denom2):
    numer3 = denom1 * numer2 + denom2 * numer1
    denom3 = denom1 * denom2
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    gcd3 = gcd(numer3, denom3)
    numer3 /= gcd3
    denom3 /= gcd3
    return [numer3, denom3]