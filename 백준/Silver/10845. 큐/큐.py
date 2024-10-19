import sys

text = [i.strip() for i in sys.stdin.readlines()][1:]
queue= []

for i in text:
    if len(i.split()) == 2:
        queue.append(int(i.split()[1]))
    elif i == 'pop':
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif i == 'size':
        print(len(queue))
    elif i == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif i == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
        
