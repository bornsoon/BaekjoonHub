a = input()
b = input()
c = input()

while True:
    if a == 'FizzBuzz':
        print('Fizz')
        break
        
        
    try:
        if a == 'Fizz':
            if int(b):
                if (int(b) + 2) % 5 == 0:
                    print('FizzBuzz')
                    break
                else:
                    print('Fizz')
                    break
    except:
        pass
    
    try:
        if a == 'Fizz':
            if int(c):
                if (int(c) + 1) % 5 == 0:
                    print('FizzBuzz')
                    break
                else:
                    print('Fizz')
                    break
    except:
        pass
    
    try:
        if b == 'Fizz' or 'FizzBuzz':
            if int(a):
                if (int(a) + 3) % 5 == 0:
                    print('Buzz')
                    break
                else:
                    print(int(a) + 3)
                    break
    except:
        pass
    
    try:
        if b == 'Fizz' or 'FizzBuzz':
            if int(c):
                if (int(c) + 1) % 5 == 0:
                    print('Buzz')
                    break
                else:
                    print(int(c) + 1)
                    break
    except:
        pass
    
    try:
        if c == 'Fizz' or 'FizzBuzz':
            if int(a):
                if (int(a) + 3) % 5 == 0:
                    print('Buzz')
                    break
                else:
                    print(int(a) + 3)
                    break
    except:
        pass
    
    try:
        if c == 'Fizz' or 'FizzBuzz':
            if int(b):
                if (int(b) + 2) % 5 == 0:
                    print('Buzz')
                    break
                else:
                    print(int(b) + 2)
                    break
    except:
        pass