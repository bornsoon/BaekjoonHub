N = int(input())
answer = 0

i = 5
while N >= i:
    answer += N // i
    i *= 5
    
print(answer)