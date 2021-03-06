# Расчет объема, площади полной и боковой поверхностей усеченного конуса
#                                                Сангинов Азамат ИУ7-11Б

# R - радиус нижнего основания усеченного конуса
# r - радиус верхнего основания усеченного конуса
# h - высота усеченного конуса
# L - образующая усеченного конуса
# Sb - площадь боковой поверхности усеченного конуса
# Sp - площадь полной поверхности усеченного конуса
# V - объем усеченного конуса

from math import pi, sqrt 

R = float(input('Введите радиус нижнего основания(R>0): '))
r = float(input('Введите радиус верхнего основания(r>0 и r!=R): '))
h = float(input('Введите высоту(h>0): '))

L = sqrt(h*h+(R-r)**2)
Sb = pi * (r + R) * L
Sp = pi* (R*R + L*(R+r) + r*r)
V = pi/3 * h * (R*R + R*r + r*r)

# Проверка введенных данных на ошибочность и вывод результата
if(R<=0 or r<=0 or h<=0 or R==r):
    print('Ошибка')
else:
    print('\nПлощадь боковой поверхности = ','{:.3f}' .format(Sb))
    print('Площадь полной поверхности = ','{:.3f}' .format(Sp))
    print('Объем усеченного конуса = ','{:.3f}' .format(V))
