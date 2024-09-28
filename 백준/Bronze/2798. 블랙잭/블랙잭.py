n, m = map(int, input().split())
card = list(map(int, input().split()))

answer = m
for i in range(n):
    if card[i] > m - 2:
        continue
    for j in range(i + 1, n):
        if card[i] + card[j] > m - 1:
            continue
        for k in range(j + 1, n):
            sum_card = card[i] + card[j] + card[k]
            if sum_card > m:
                continue
            if m - sum_card < answer:
                answer = m - sum_card
print(m - answer)