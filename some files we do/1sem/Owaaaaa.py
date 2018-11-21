x = float(input('X = '))
eps = float(input('eps = '))
nmax = int(input('NMax = '))
step = int(input('Step = '))

n = 0
t = el = s = 1
gr = -1

if abs(t) > eps:
    print('\u250c' ,'\u2500' *10, '\u252C','\u2500' *9,'\u252C','\u2500' *17,sep = '',end = '')
    print('\u252C','\u2500' *14,'\u2510', sep = '')
    print('\u2502№ Итерации\u2502X текущий\u2502Текущий член ряда\u2502Текущая сумма','\u2502')
    print('\u251c' ,'\u2500' *10, '\u253c','\u2500' *9,'\u253c','\u2500' *17,sep = '',end = '')
    print('\u253c','\u2500' *14,'\u2524', sep = '')
    el = -1

while abs(t) >= eps:
    n += 1
    t *= x*(-0.5)*((2*n-1))/ n
    s += t
    if n%step == 0:
        print('\u2502','{:8d}'.format(n),'\u2502',end = '')
        if abs(x) > 1000:
            print('{:8.2e}'.format(x),'\u2502',end = '')
        else:
            print('{:8.2f}'.format(x),'\u2502',end = '')
        if abs(t) > 1000:
            print('{:16.4e}'.format(t),'\u2502',end = '')
        else:
            print('{:16.4f}'.format(t),'\u2502',end = '')
        if abs(s) > 1000:
            print('{:13.2e}'.format(s),'\u2502')
        else:
            print('{:13.2f}'.format(s),'\u2502')
    if n == nmax:
        gr = 1
        break

if el < 0:
    print('\u2514' ,'\u2500' *10, '\u2534','\u2500' *9,'\u2534','\u2500' *17,sep = '',end = '')
    print('\u2534','\u2500' *14,'\u2518', sep = '')
    print()

if gr == 1:
    print('Ряд не сошелся за ', n, 'итераций')
else:
    print('Ряд сошелся за ', n, 'итераций')
if s > 1000:
    print('Сумма ряда =','{:4.2e}'.format(s))
else:
    print('Сумма ряда =','{:4.2f}'.format(s))


































































