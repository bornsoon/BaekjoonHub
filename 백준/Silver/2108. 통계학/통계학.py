import sys

n = int(input())

lst = [int(i) for i in sys.stdin.readlines()]
sorted_lst = sorted(lst)
dict = {}

for i in sorted_lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

max_dict = max(dict.values())

max_lst = []
for key, value in dict.items():
    if value == max_dict:
        max_lst.append(key)

max_lst.sort()
max_value = ()
if len(max_lst) > 1:
    max_value = max_lst[1]
else:
    max_value = max_lst[0]

if sum(lst) < 0:
    print(int(sum(lst) / n - 0.5))
else:
    print(int(sum(lst) / n + 0.5))
print(sorted_lst[int(n/2)])
print(max_value)
print(sorted_lst[-1] - sorted_lst[0])