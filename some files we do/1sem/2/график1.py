# Программа для вычисления таблицы значений трех функций и вывода графика одной 
# из них.


# b - аргумент 
# s1,s2,s3 - значения функций
# b1,b2 - начальное и конечное значение аргумента
# shag - шаг
# u1,u2,u3,u4,u5,u6,u7,u8 - коды символов в юникод
# S1 - список значений функции s1
# B - список значений аргумента
# k - рабочая переменная
# mi,ma - минимум и максимум функции s1
# flag - рабочая переменная
# i - рабочая переменная
# m1, m2, m - номер знака в строке

from math import sqrt, log, fabs

b1 = float(input('Введите начальную границу аргумента:'))
shag = float(input('Введите шаг:'))
b2 = float(input('Введите конечную границу агрумента:'))

u1 = '\u250C'
u2 = '\u2500'
u3 = '\u252C'
u4 = '\u2502'
u5 = '\u2534'
u6 = '\u2510'
u7 = '\u2514'
u8 = '\u2518'
u9 = '\u253C'

z = u1+u2*5+u3+u2*9+u3+u2*13+u3+u2*13+u3+u2*13+u6
print(z)
print(u4,' № ',u4,'   b   ',u4,'     s1     ',end=u4)
print('     s2     ',u4,'    s3     ',u4)

#Подсчет значений функций, вывод таблицы значений, запись значений функйии s1
#в список.
S1=[]
B=[]
b = b1
k = 1
while b <= b2+shag/2: 
    s1 = b*b*b + 9.57*b*b-243.7*b+773.6
    if b > 0:
        s2 = b*log(b)-18
        s3 = sqrt(fabs(s1-s2))
        print('\u2502',end='')
        print('{:4d}'.format(k),u4,'{:8.3f}'.format(b),end=u4)
        print('{:13.4f}'.format(s1),end=u4)
        print('{:13.4f}'.format(s2),end=u4) 
        print('{:13.4f}'.format(s3),end='\u2502\n')
    else:
        s2 = 'Не существует'
        s3 = 'Не существует'
        print('\u2502',end='')
        print('{:4d}'.format(k),u4,'{:8.3f}'.format(b),end=u4)
        print('{:13.4f}'.format(s1),end=u4)
        print(s2,end=u4)
        print(s3,end='\u2502\n')
    S1.append(s1)
    B.append(b)
    b += shag
    k += 1
z = u7+u2*5+u5+u2*9+u5+u2*13+u5+u2*13+u5+u2*13+u8
print(z)

print()

ma = max(S1)
mi = min(S1)


print()
#Подсчет наименьшего значения функции. Вывод оси s1
flag = 1
for i in range (len(S1)):
    if S1[i] >= 0:
        if flag:
            k = S1[i]
            flag = 0
        elif S1[i] < k:
            k= S1[i]

m2 = (k-mi)/(ma-mi)*59+1
m2 = round(m2)

#Вывод значений s1 на оси координат.
print(' '*7,end='')
flag=1
h = (ma-mi)/10
h = round(h)
min1 = round(mi)
for i in range(0,11):
    print('{:6d}'.format(min1),end='')
    min1 += h
print()
print(' '*10,end='')
k = 0
for i in range (1,65):
    if i == m2:
        print(u3,end='')
        if i == 2+6*k:
            k +=1
    elif i == 2+6*k:
        print(u9,end='')
        k +=1
    else:
        print(u2,end='')

print('\u2192','s1')

#Построение графика
for i in range (len(B)):
    print('{:9.4f}'.format(B[i]),end ='')
    m = (S1[i] - mi)/(ma-mi)*59+1
    m = round(m)
    if m == m2 or m == m2-1:
        print(' '*(m-1),'*')
    elif m < m2:
        print(' '*(m-1),'*',end='')
        print(' '*(m2-m-2),u4)
    else:
        print(' '*(m2-1),u4,end='')
        print(' '*(m-m2-1),'*')  
print(' '*(m2+8),'\u2193')
print(' '*(m2+8),'b')
print()

b = b1 + S1.index(mi)*0.1
print('Наименьший элемент s1:','{:7.4f}'.format(mi))
print('Значение b, при котором достигается минимум s1:', end='')
print('{:7.3f}'.format(b))

