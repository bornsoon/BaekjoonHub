n, k = map(int, input().split())

lst = [i+1 for i in range(n)]

answer = []
idx = 0

while(lst):
    idx += k - 1
    while(idx >= len(lst)):
        idx -= len(lst)
    answer.append(lst[idx])
    del lst[idx]
        
print(f"<{', '.join(map(str, answer))}>")