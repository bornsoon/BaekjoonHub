while True:
    x = input()
    flag = True
    if x == '0':
        break
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            print("no")
            flag = False
            break
    if flag:
        print("yes")