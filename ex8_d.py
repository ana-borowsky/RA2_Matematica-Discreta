def D(x):
    if x <= 3:
        if x == 1:
            return 0
        elif x == 2:
            return D(1) - 1
        elif x == 3:
            return D(1) + 1
    else:
        if x % 2 == 0:
            return D(x - 2) - 1 
        else:
            return D(x - 2) + 1

print('p' + '%+d' % D(3) + 'q')