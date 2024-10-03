n = int(input())
nlst = [i for i in range(1 , n + 1)]

while(len(nlst) > 1):
    if len(nlst) % 2 == 0:
        del nlst[0::2]
    else:
        nlst.append(nlst[1])
        del nlst[0::2]
        if len(nlst) > 1:
            del nlst[0]
        else:
            break
print(nlst[0])