from math import sin,cos
from decimal import *


def in_function(x):
    return x-1


def calc_pram(a,b,n,eps):
    n = n
    n1 = n*2
    if a<0 and b>0:
        resu = calc_pram(a,0,n,eps) + calc_pram(0,b,n,eps)
        return resu
    else:
        while abs(calc_integra(a,b,n) - calc_integra(a,b,n1)) >= eps:
            n = n1
            n1 = n1*2
        return calc_integra(a,b,n1)


def calc_integra(a,b,n):
    res = 0
    h = (b-a)/n
    for i in range(n):
        res+=in_function(a + h * (i + 0.5))
    res *= h
    return res

def calc_3(a,b,n,eps):
    n = n
    n1 = n*2
    if a<0 and b>0:
        resu = calc_3(a,0,n,eps) + calc_3(0,b,n,eps)
        return resu
    else:
        while abs(calc_integra3(a,b,n) - calc_integra3(a,b,n1)) >= eps:
            n = n1
            n1 = n1*2
        return calc_integra(a,b,n1)


def calc_integra3(a,b,n):
    res = in_function(a)+in_function(b)
    m = n*3 - 1
    h = (b-a)/n*3
    for i in range(m):
        x = a + h*i
        if i%3==0:
            res+=2*in_function(x)
        else:
            res+=3*in_function(x)
    res = 3/8 *res * h
    return res

def calc_4(a,b,n,eps):
    n = n
    n1 = n*2
    if a<0 and b>0:
        resu = calc_4(a,0,n,eps) + calc_4(0,b,n,eps)
        return resu
    else:
        while abs(calc_integra4(a,b,n) - calc_integra4(a,b,n1)) >= eps:
            n = n1
            n1 = n1*2
        return calc_integra(a,b,n1)


def calc_integra4(a,b,n):
    res = 0
    h = (b-a)/n
    for i in range(n):
        res+=1
        
    return res


def calc_trap(a,b,n,eps):
    n = n
    n1 = n*2
    if a<0 and b>0:
        resu = calc_trap(a,0,n,eps) + calc_trap(0,b,n,eps)
        return resu
    else:
        while abs(calc_integra1(a,b,n) - calc_integra1(a,b,n1)) >= eps:
            n = n1
            n1 = n1*2
        return calc_integra1(a,b,n1)


def calc_integra1 (a,b,n):
    res = (in_function(a)+in_function(b))/2
    h = (b-a)/n
    for i in range(1,n):
        res += in_function(a + h*i)
    res *= h
    return res


def checko(a):
    l = 0
    if len(a)==0 or a.isspace():
        print('Разрешено вводить только неотрицательные числа числа!!')
        return 0,-1
    for k in range(len(a)):
        if ord(a[k]) in range(48,59):
            continue
        elif a[k] == '.' and ord(a[k+1]) in range(48,59) and ord(a[k-1]) in range(48,59):
            continue
        elif a[k] == '-' and ord(a[k+1]) in range(48,59):
            continue
        else:
            l = -1
            break
    if l < 0:
        print(l)
        return(print('Разрешено вводить только числа!!')),l
    else:
        a = float(a)
    return a,l


def checko1(n):
    abc = ('0123456789')
    l = 0
    if len(n)==0 or n.isspace() or n == '0':
        print('Разрешено вводить только целые неотрицательные числа числа!!')
        return 0,-1
    for i in n:
        if abc.find(i)<0:
            l = -1
            break
    if l < 0:
        return(print('Разрешено вводить только целые неотрицательные числа числа!!')),l
    else:
        n = int(n)
    return n,l


         
l1 = 0
l2 = 0
a = input("Левая граница: ")
a,l1 = checko(a)
if l1 >= 0:
    b = input('Правая граница: ')
    b,l2 = checko(b)
    if l2 >= 0:
        l3 = 0
        n = input('Разбиение1: ')
        n,l3 = checko1(n)
        if l3 >= 0:
            l4 = 0
            n1 = input('Разбиение2: ')
            n1,l4 = checko1(n1)
            if l4 >= 0:
                eps = float(input('eps '))
                integral = calc_integra(a,b,n)
                integra2 = calc_integra1(a,b,n)
                integra3 = calc_integra(a,b,n1)
                integra4 = calc_integra1(a,b,n1)
                print(calc_3(a,b,n,eps))
                print(calc_4(a,b,n,eps))
                print('\u250c' ,'\u2500' *11, '\u252C','\u2500' *26,'\u252C','\u2500' *26,sep = '',end = '')
                print('\u2510', sep = '')
                print('\u2502 Разбиения \u2502 Срединные прямоугольники \u2502 Трапеция ',' '*14,'\u2502')
                print('\u251c' ,'\u2500' *11, '\u253c','\u2500' *26,'\u253c','\u2500' *26,sep = '',end = '')
                print('\u2524', sep = '')
                print('\u2502','{:9d}'.format(n),'\u2502',end = '')
                print('{:25.8f}'.format(integral),'\u2502',end = '')
                print('{:25.8f}'.format(integra2),'\u2502')
                print('\u251c' ,'\u2500' *11, '\u253c','\u2500' *26,'\u253c','\u2500' *26,sep = '',end = '')
                print('\u2524', sep = '')
                print('\u2502','{:9d}'.format(n1),'\u2502',end = '')
                print('{:25.8f}'.format(integra3),'\u2502',end = '')
                print('{:25.8f}'.format(integra4),'\u2502')
                print('\u2514' ,'\u2500' *11, '\u2534','\u2500' *26,'\u2534','\u2500' *26,sep = '',end = '')
                print('\u2518', sep = '')

                if abs(integra3-integral) < abs(integra4-integra2):
                    print('Метод прямоугольников с точностью ',eps,': ',round((calc_pram(a,b,n,eps)),5))
                else:
                    print('Метод трапеций с точностью ',eps,': ',round((calc_trap(a,b,n,eps)),5))


                
