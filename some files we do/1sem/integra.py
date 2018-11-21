from math import sin,pi

def in_function(x):
    return sin(x)

def calc_integra(a,b,n,eps):
    res = 0
    h = (b-a)/n
    i = 0
    while abs(res)>=eps:
        res+=in_function(a+h*(i+0.5))
        res *= h
        i+=1
    return res

print('sin(x)')
a = float(input('Начальное значение: '))
b = float(input('Конечное значение: '))
n = int(input('Разбиение: '))
eps = float(input('eps '))
integral = calc_integra(a,b,n,eps)
print(integral)
