# Программа для расчета значений функции в заданном интервале с заданным шагом
# и для построения графика одной из функций
#                                                       Сангинов Азамат ИУ7-11

# an,d - начальное значение
# s = шаг
# ak - конечное значение
# m - количество шагов
# x - список значений аргумента
# c - список значений функции c2
# diap - количество значений, удовлетворяющих условию
# mi, min1 , ma - минимум и максимум функции c2
# flag, i, ml,m2, h - рабочие переменные

from math import sin

print('Функция c1 имеет вид: ',end = ' ')
print('c1 = 4.05*a^4 + 12.6*a^3 + 8.8*a^2 + 11.2*a + 17.6')
print('\nФункция c2 имеет вид: ',end = ' ')
print('c2 = a^2 + 4*sin(a)\n')

an = float(input('Введите начальное значение: '))
ak = float(input('Введите конечное значение: '))
s = float(input('Ввежи'))
m = int(abs((ak-an)/s)+1)

#print('\u250c' , '\u2500' *67,'\u2510', sep = '')
#print('\u2502  x', ' ' *26,'c1',' '*22,'c2',' '*6, '\u2502')
#print('\u251c', '\u2500' *67,'\u2524', sep = '')
#diap = 0
d = an

x = []
for i in range(m):
    x.insert(i,an)
    i+=1
    if d>0:
        an -= s
    else:
        an += s
c = []
mi = an*an + 4*sin(an)
ma = an*an + 4*sin(an)
for i in range (m):
    #print ('\u2502','{:7.1f}'.format((x[i])),'   ', end = ' ')
    #c1 = 4.05*x[i]**4 + 12.6*x[i]**3 + 8.8*x[i]**2 + 11.2*x[i] +17.6
    #if -3 <= c1 <= 0:
        #diap+=1
    c2 = x[i]*x[i]# + 4*sin(x[i])
    c.insert(i,c2)
    if c2>=ma:
        c2,ma = ma,c2
    if c2<= mi:
        c2,mi = mi,c2
    #print('{:20.3f}'.format(c1),'{:20.3f}'.format(c2),' '*10, ' \u2502')
#print('\u2514', '\u2500' *67, '\u2518',sep = '')
#print('\nКоличество значений в диапазоне -3 <= c1 <= 0 :', diap)
print()

flag = 1
for i in range (len(c)):
    if c[i] >= 0:
        if flag:
            k = c[i]
            flag = 0
        elif c[i] < k:
            k= c[i]

m2 = (k-mi)/(ma-mi)*59+1
m2 = round(m2)

print(' '*4,end='')
flag=1
h = (ma-mi)/10
h = round(h)
min1 = round(mi,2)
for i in range(0,7):
    print('{:9.2f}'.format(min1),end='')
    min1 += h
print()
print(' '*10,end='')
k = 0
for i in range (1,65):
    if i == m2:
        print('\u252C',end='')
        if i == 2+6*k:
            k +=1
    elif i == 2+6*k:
        print('\u253C',end='')
        k +=1
    else:
        print('\u2500',end='')

print('\u2192','c1')

#Построение графика
for i in range (len(x)):
    print('{:9.4f}'.format(x[i]),end ='')
    m = (c[i] - mi)/(ma-mi)*59+1
    m = round(m)
    if m == m2 or m == m2-1:
        print(' '*(m-1),'*')
    elif m < m2:
        print(' '*(m-1),'*',end='')
        print(' '*(m2-m-10),'\u2502')
    else:
        print(' '*(m2-1),'\u2502',end='')
        print(' '*(m-m2-1),'*')  
print(' '*(m2+8),'\u2193')
print(' '*(m2+8),'x')
print()

'''ma = int(ma)
mi = int(mi)
f = 1
for i in range (len(c)):
    if c[i] >= 0:
        if f:
            k = c[i]
            f = 0
        elif c[i] < k:
            k = c[i]

m2 = (k-mi)/(ma-mi)*59
m2 = round(m2)
print('////',m2,'\\\\')
print(' '*7,end='')

r = int((ma-mi)/10)

min1 = int(mi)
for i in range(1,11):
    print('{:6d}'.format(min1),end='')
    min1 += r
print()

print(' '*10,end='')
k = 0
for i in range (1,68):
    if i == m2:
        print('',end='')
        if i == 10+6*k:
            k +=1
    elif i == 2+6*k:
        print('\u253C',end='')
        k +=1
    else:
        print('\u2500',end='')

print('\u2192','c2')

for i in range (len(x)):
    print('{:7.1f}'.format(x[i]),end ='')
    m = (c[i] - mi)/(ma-mi)*59+1
    m = round(m)
    if abs(m) == abs(m2):
        print(' '*(m-1),'*')
    elif abs(m) < abs(m2):
        print(' '*(m-1),'*',end='')
        print(' '*(m2-m-1),'\u2502')
    elif abs(m)>m2:
        print(' '*(m2+2),'\u2502',end='')
        print(' '*(abs(m2-m)+1),'*')  
print(' '*(m2+9),'\u2193')
print(' '*(m2+9),'x')'''
