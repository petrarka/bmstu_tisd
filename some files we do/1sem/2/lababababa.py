from math import sin
print('Функция c1 имеет вид: ',end = ' ')
print('c1 = 4.05*a^4 + 12.6*a^3 + 8.8*a^2 + 11.2*a + 17.6')
print('\nФункция c2 имеет вид: ',end = ' ')
print('c2 = a^2 + 4*sin(a)\n')

a1 = float(input('Введите начальное значение: '))
n = int(a1/0.1)
print(4*sin(0))

print('\u250f', '\u2501' *21, '\u2513', sep = '')
print('\u2503  a           c1          c2      \u2503')
print('\u2523', '\u2501' *21, '\u252b', sep = '')
diap = 0
for i in range (n,0,1):
    a = i/10
    print ('\u2503',a,'   ', end = '')
    c1 = 4.05*a**4 + 12.6*a**3 + 8.8*a**2 + 11.2*a +17.6
    if -3 <= c1 <= 0:
        diap+=1
    c2 = a*a + 4*sin(a)
    print(' ','{:7.4f}        {:7.4f}'.format(c1,c2),'\u2503')
print('\u2503  0.0      17.6000         0.0000 \u2503')
print('\u2517', '\u2501' *21, '\u251b',sep = '')

print('\nКоличество значений в диапазоне -3 <= c1 <= 0 :', diap)
