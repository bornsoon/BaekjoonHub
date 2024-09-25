import copy

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)
    
arr2 = copy.deepcopy(arr)

num = []
stk = []
pr = []

for i in range(1, n + 1):
    if arr:
        if i != arr[0]:
            stk.append(i)
            pr.append("+")
        else:
            arr.remove(i)
            num.append(i)
            pr.append("+")
            pr.append("-")
    
            if stk and arr:                
                while stk[-1] == arr[0]:
                    stk.pop()
                    num.append(arr[0])
                    arr.remove(arr[0])
                    pr.append("-")
                    if not stk or not arr:
                        break

if num == arr2:
    for i in pr:
        print(i)
else:
    print("NO")