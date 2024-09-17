N = int(input())
dict = {}
for i in range(N):
    _ = input()
    dict[_] = len(_)
    
sorted_d = sorted(dict.items(), key=lambda x: (x[1], x[0]))
for i in sorted_d:
    print(i[0])