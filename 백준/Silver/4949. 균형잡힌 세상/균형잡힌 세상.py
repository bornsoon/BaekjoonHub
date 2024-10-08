import sys

text = sys.stdin.readlines()
parenthesis1 = {'(': 'S', '[': 'L' }
parenthesis2 = {')': 'S', ']': 'L' }

for line in text:
    line = line.rstrip()
    if line == '.':
        break

    temp = [0]
    current = ''

    for j in line:
        if j in parenthesis1.keys():
            if current == parenthesis1[j]:
                temp[-1] += 1
            else:
                current = parenthesis1[j]
                temp.append(1)
        elif j in parenthesis2.keys():
            if current == parenthesis2[j]:
                temp[-1] -= 1
                if temp[-1] == 0:
                    temp.pop()
                    if temp[-1] > 0:
                        if current == 'S':
                            current = 'L'
                        elif current == 'L':
                            current = 'S'
                    else:
                        current = ''
            elif current != parenthesis2[j]:
                temp.append(-1)
                break
    if temp[-1] != 0:
        print('no')
    else:
        print('yes')