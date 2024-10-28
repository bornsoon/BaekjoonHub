T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    arr = input().lstrip('[').rstrip(']').split(',')
    if arr == ['']:
        arr = []

    psize = len(p)
    flag = True
    R = False

    for j in range(psize):
        if p[j] == 'R':
            if R:
                R= False
                continue
            else:
                R = True
                continue
        elif p[j] == 'D':
            if arr:
                if not R:
                    arr.pop(0)
                else:
                    arr.pop(-1)
            else:
                print("error")
                flag = False
                break
    if flag:
        print("[", end="")
        if not R:
            s = ','.join([arr[i] for i in range(len(arr)-1)])
            if arr:
                if len(arr) == 1:
                    print(f"{arr[-1]}]")
                else:
                    print(f"{s},{arr[-1]}]")
            else:
                print("]")
        else:
            s = ','.join([arr[i] for i in range(len(arr) -1, 0, -1)])
            if arr:
                if len(arr) == 1:
                    print(f"{arr[0]}]")
                else:
                    print(f"{s},{arr[0]}]")
            else:
                print("]")
