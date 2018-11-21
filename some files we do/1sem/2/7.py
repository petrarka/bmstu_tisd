# Программа для вычисления таблицы значений функции и построения ее графика


# x,b - начальная точка
# k - конечная точка
# n - шаг по ординате
# t,a,g,h,S,L,o -графические переменные
# maxim,minim - максимальное и минимальное значение функции
# F - значение функции
# Y - шаг по абсциссе
# i - вспомогательная переменная

b,k,n = map(float,input('Введите начальную точку, конечную точку и шаг: ')\
          .split())

t = ('\u2981')
a = ('\u2579')
g = ('\u2501')
h = ('\u2503')
o = ('\u254B')
S = ('\u250F') + g*59 + ('\u2513')
L = ('\u2517') + g*59 + ('\u251B')

print(S) # построение таблицы
print(h,'Номер',a,' Аргумент',a,'              \u03B3(b)                   ',h)

N = 1.0 
minim = ((((((((b+34)*b-2)*b+24)*b-76)*b+33)*b-1)*b+3)*b+7)*b-33
maxim = ((((((((b+34)*b-2)*b+24)*b-76)*b+33)*b-1)*b+3)*b+7)*b-33
x = b
while k >= b:
    F = ((((((((b+34)*b-2)*b+24)*b-76)*b+33)*b-1)*b+3)*b+7)*b-33
    print(h,'{:5.0f}'.format(N),a,'{:9.4f}'.format(b),a,'{:37.4f}'.format(F),h)
    N += 1
    b = round(b+n,4)
    if F > maxim:
        maxim = F
    if F < minim:
        minim = F
        
print(L)

maxim = int(maxim) # нахождение шага по ординате
minim = int(minim)
Y = int(abs(maxim - minim)//14)
maxim += 2*Y


print('\n','         ',sep = '',end = '') # построение графика
for i in range (minim,maxim,Y):
    if i-Y < 0 < i and minim < 10 and i != minim:
        print('   0',sep ='',end = '')
    else:
        print('{:4.0f}'.format(i),sep ='',end = '')

print('\n','         ',sep = '',end = '')
for i in range (minim,maxim,Y):
    print(g*3,o,sep ='',end = '')
print(' \u03B3')

while k >= x:
    print('{:9.4f}'.format(x),sep = '',end = '')
    F = ((((((((x+34)*x-2)*x+24)*x-76)*x+33)*x-1)*x+3)*x+7)*x-33
    for i in range (minim,maxim,Y):
        if i - Y < F <= i:
            print('   ',t,sep ='',end = '')
        elif i-Y < 0 <= i and minim < Y and i != minim :
            print('   ',h,sep ='',end = '')
        else:
            print('    ',sep ='',end ='')
    x = round(x+n,4)
    print()

print('         ',sep = '',end = '')
for i in range (minim,maxim,Y):
   if i-Y < 0 <= i and i != minim:
       print('   b')
   else:
       print('    ',sep ='',end ='')

    
    

