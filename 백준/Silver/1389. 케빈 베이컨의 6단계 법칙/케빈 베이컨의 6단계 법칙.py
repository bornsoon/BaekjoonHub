N, M = map(int, input().split())

rel = [set() for i in range(N)]

for i in range(M):
    v, w = map(int, input().split())
    rel[v-1].add(w-1)
    rel[w-1].add(v-1)

answer = []

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        st = rel[i]
        
        while(True):
            count += 1
            s = set()
            if j in st:
                break
            else:
                for k in st:
                    s.update(rel[k])
                st = s
    
    answer.append(count)

print(answer.index(min(answer)) + 1)