n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

print(sum(scores) / (n * max_score) * 100)