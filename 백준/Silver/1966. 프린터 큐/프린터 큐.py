test_case = int(input())

for i in range(test_case):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 1
    
    while(True):
    
        if lst[0] != max(lst):
            lst.append(lst[0])
            lst.pop(0)
            m -= 1
            if m == -1:
                m += len(lst)
        else:
            if m == 0:
                print(count)
                break
            else:
                lst.pop(0)
                m -= 1
                count += 1