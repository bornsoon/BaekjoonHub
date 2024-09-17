N = int(input())
lst = []
for i in range(N):
    _ = input().split()
    lst.append((int(_[0]), _[1], i))
    
sorted_l = sorted(lst, key=lambda x: (x[0], x[2]))
for i in sorted_l:
    print(i[0], i[1])