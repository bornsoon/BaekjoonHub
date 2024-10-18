import sys

text = [i.strip() for i in sys.stdin.readlines()][1:]
stk = []

for i in text:
    if len(i.split()) == 2:
        stk.append(int(i.split()[1]))
    elif i == 'pop':
        if stk:
            print(stk[-1])
            stk.pop()
        else:
            print(-1)
    elif i == 'size':
        print(len(stk))
    elif i == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)
        
