# Программа для вычисления квадратного уравнения
#                       Сангинов Азамат ИУ7-11Б

from math import sqrt

# a, b, c - коэфициенты уравнения
# d - дискриминант
# x - корень квадратного уравнения

print('Квадратное уравнение имеет вид: a*x^2 + b*x + c = 0')

a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

# Проверка коэффициентов и вывод результатов
if(a != 0):
    d = b*b - 4*a*c
    if (d == 0):
        x = -b/2*a
        print('Корень кратности 2: x = ','{:.3f}' .format(x))
    elif (d > 0):
        x = (-b + sqrt(d))/2*a
        print('x1 = ','{:.3f}' .format(x))
        x = (-b - sqrt(d))/2*a
        print('x2 = ','{:.3f}' .format(x))
    elif (d < 0):
        print('Нет действительных решений')
elif( a == 0 and b != 0):
    x = -c/b
    print('Линейное уравнение: x = ','{:.3f}' .format(x))
elif( a == 0 and b == 0 and c == 0):
    print('x - любое число')
elif( a == 0 and b == 0 and c != 0):
    print('Нет решений')