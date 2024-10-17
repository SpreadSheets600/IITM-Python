# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()

if task == 'factors':
    n = int(input())
    if (n > 0):
        for i in range(1, n + 1):
            if (n % i == 0):
                print(i)

elif task == 'find_min':
    n = int(input())
    min = 99999999999999999
    num = int(input())
    if (n > 1):
        while (n > 1):
            if num < min:
                min = num
            num = int(input())
            n -= 1
    else:
        min = num
    print(min)

elif task == 'prime_check':
    num = int(input())
    flag = False
    if (num > 0):
        if (num == 2):
            flag = True
        else:
            for i in range(3, num + 1):
                for j in range(2, i):
                    if (i % j == 0):
                        flag = False
                        break
                    else:
                        flag = True
        print(flag)

elif task == 'is_sorted':
    s= input()
    flag = True
    for i in range(len(s) - 1):
        if (s[i] > s[i + 1]):
            flag = False
            break
    print(flag)

elif task == 'any_true':
    n = int(input())
    num = int(input())
    flag = False
    while(n > 1):
        if(num % 3 == 0):
            flag = True
        n -= 1
        num = int(input())
    print(flag)

elif task == 'manhattan':
    direction = input()
    x_distance, y_distance = 0, 0
    while (direction != 'STOP'):
        if (direction =='LEFT'):
            x_distance -= 1
        elif (direction == 'RIGHT'):
            x_distance += 1
        elif (direction == 'UP'):
            y_distance += 1
        elif (direction == 'DOWN'):
            y_distance -= 1
        x, y = abs(x_distance - 0), abs(y_distance - 0)
        manhattan_distance = x + y
        direction = input()
    print(manhattan_distance)