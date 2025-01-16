def solution(polynomial):
    term = polynomial.split(' + ')
    x = 0
    y = 0
    for i in term:
        if 'x' in i:
            if i.strip('x') != '':
                x += int(i.strip('x'))
            else:
                x += 1
        else:
            y += int(i)
    if '+' in polynomial:
        if x > 1:
            if y > 0:
                return f'{x}x + {y}'
            elif y == 0:
                return f'{x}x'
        elif x == 1:
            if y > 0:
                return f'x + {y}'
            elif y == 0:
                return 'x'
        else:
            return f'{y}'
    elif 'x' in polynomial:
        if x > 1:
            return f'{x}x'
        else:
            return 'x'
    else:
        return f'{y}'