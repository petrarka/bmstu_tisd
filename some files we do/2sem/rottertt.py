from math import *
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt

## h*.. - элементы интерфейса
## x0, x1 - края интервала, eps - точность,
## nmax - максимальное число итераций
## a,b - края отрезка, step - шаг
## ans - значения корня, itter - количество итераций,
## inter - интервал

## Функция
def f(x):
    return x**2-4

def der_f(x):
    return np.cos(x)

## Метод
def secant(f, x1, x0, eps, nmax):
   n = 1
##   print('===')
   while n <= nmax:
      x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
##      print(x1,x2)
      if abs(x2-x1) < eps:
         return x2,n
      else:
         x0 = x1
         x1 = x2
      n += 1
   return '**',0

## Разбиение на участки
def tabul(a,b,step,eps,nmax):
  ans = []
  t = a
  itter = []
  inter = []
  n = 0
  i = 0
  while a < b:
    t = a
    a += step
##    print('*',t,'=',a)
    if f(t) * f(a) <= 0:
##       print(f(t) * f(a))
       x,i = secant(f,t,a,eps,nmax)
##       print(n,'-',t,'<',x,'<=',a,'f(x)',f(x))
       n+=1
       if x == '**':
          s = '[' + str(t) + ';' + str(a) + ']'
          ans.append('+')
          itter.append('+')
          inter.append(s)
       elif (t<=x<a):
         s = '[' + str(t) + ';' + str(a) + ']'
         itter.append(i)
         ans.append(x)
         inter.append(s)
       else:
         ans.append('*')
         itter.append('*')
         inter.append('*')
    else:
       ans.append('-')
       itter.append('-')
       inter.append('-')
    if a > b:
        return ans,itter,inter
##    t = a

  return ans,itter,inter

## Построение графика
def show_graph():
    a = float(left.get())
    b = float(right.get())
    step = float(steph.get())
    nmax = int(nmaxh.get())
    eps = float(epsh.get())
    y = np.linspace(a,b,100)
    plt.grid(True)
    line, = plt.plot(y, f(y), lw=2)
    maf = max(f(y))
    mif = min(f(y))
    ans, itter, inter = tabul(a,b,step,eps,nmax)
    for i in range (len(y) - 1):
        if f(y[i-1]) < f(y[i]) > f(y[i+1]) and fabs(f(y[i]) - maf) < 0.005 or f(y[i-1]) > f(y[i]) < f(y[i+1]) and fabs(f(y[i]) - mif) < 0.005:
            point, = plt.plot(y[i], f(y[i]),'ro', markersize = 9)
##       if f(i) == maf or f(i) == mif or fabs(f(i) - maf) <= 0.005 or fabs(f(i) - mif) <= 0.005:
##            point, = plt.plot(i, f(i),'ro', markersize = 9)
##        if f(y[i-1]) < f(y[i]) < f(y[i+1]):
##            point, = plt.plot(i, f(i),'ro', markersize = 9)
             
    for i in ans:
        if i != '*' and i != '-':
            point, = plt.plot(float(i), f(float(i)),'ro', markersize = 9)
    plt.show()

## Построение таблицы
def table(ans, itter, inter):
##   print(ans)
##   print(itter)
##   print(inter)
   it = 0
   for i in range(len(ans)):
      n = i +5
      if ans[i] == '+':
         h0 = Label(root, text = str(i+1), width = 10,borderwidth=2, relief="solid")
         h0.grid(row = n, column = 1)
         h01 = Label(root, text = inter[i], width = 10,borderwidth=2, relief="solid")
         h01.grid(row = n, column = 2)
         h02 = Label(root, text = 'Превышение', width = 10,borderwidth=2, relief="solid")
         h02.grid(row = n, column = 4)
         h03 = Label(root, text = 'Превышение', width = 10,borderwidth=2, relief="solid")
         h03.grid(row = n, column = 3)
         h04 = Label(root, text = 'Превышение', width = 10,borderwidth=2, relief="solid")
         h04.grid(row = n, column = 5)
         h04 = Label(root, text = '1', width = 10,borderwidth=2, relief="solid")
         h04.grid(row = n, column = 6)
         it += 1
         #print(inter[i],'|','Превышение','|','Превышение','|','Превышение','Превышение')
      elif ans[i] != '-' and ans[i] != '*':
##         print(inter[i],'|','|',ans[i],'|',f(ans[i]),'|',itter[i])
         s = str("%.e" % (f(ans[i])))
         an = str("%.6f" % ans[i])
         #an = str(round(ans[i],6))
         h0 = Label(root, text = str(i+1), width = 10,borderwidth=2, relief="solid")
         h0.grid(row = n, column = 1)
         h01 = Label(root, text = inter[i], width = 10,borderwidth=2, relief="solid")
         h01.grid(row = n, column = 2)
         h02 = Label(root, text = s, width = 10,borderwidth=2, relief="solid")
         h02.grid(row = n, column = 4)
         #print(s)
         h03 = Label(root, text = an, width = 10,borderwidth=2, relief="solid")
         h03.grid(row = n, column = 3)
         h04 = Label(root, text = str(itter[i]), width = 10,borderwidth=2, relief="solid")
         h04.grid(row = n, column = 5)
         h04 = Label(root, text = '0', width = 10,borderwidth=2, relief="solid")
         h04.grid(row = n, column = 6)
         it += 1
   if it == 0:
        messagebox.showwarning("Warning","Нет корней на данном отрезке")
        return False
   return True

## Проверка вещественных чисел
def checko(a):
    l = 0
    if len(a)==0 or a.isspace():
        return False
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
        return False
    else:
        a = float(a)
    return True

## Проверка целых чисел
def checko1(n):
    abc = ('0123456789')
    l = 0
    if len(n)==0 or n.isspace() or n == '0':
        return False
    for i in n:
        if abc.find(i)<0:
            l = -1
            break
    if l < 0:
        return False
    else:
        n = int(n)
    return True

## Запуск
def starto():
    a = left.get()
    b = right.get()
    step = steph.get()
    nmax = nmaxh.get()
    if checko(a) and checko(b) and checko(step) and checko1(nmax):
        a = float(a)
        b = float(b)
        step = float(step)
        nmax = int(nmax)
    else:
        messagebox.showwarning("Warning","Ошибка ввода")
        return False
    if a > b:
        a, b = b, a
    elif a == b:
        messagebox.showwarning("Warning","Ошибка ввода")
        return False
    if b - a < step:
        messagebox.showwarning("Warning","Несоответсвующий шаг")
        return False
    if epsh.get().isspace():
        return False
    eps = float(epsh.get())
    ans, itter, inter = tabul(a,b,step,eps,nmax)
##    print(f(ans[3]))
##    print(itter)
##    print(inter)
    table(ans, itter, inter)


root = Tk()
root.title("График функции")
#root.minsize(640 , 170)
#root.resizable(width = True, height = True)

h1 = Label(root, text = 'От', width = 10)
h1.grid(row = 1, column = 1)
left = Entry(root, width = 10)
left.grid(row= 2, column = 1)
h2 = Label(root, text = 'До', width = 10)
h2.grid(row = 1, column = 2)
right = Entry(root, width = 10)
right.grid(row= 2, column = 2)
h3 = Label(root, text = 'Шаг', width = 10)
h3.grid(row = 1, column = 3)
steph = Entry(root, width = 10)
steph.grid(row= 2, column = 3)
h4 = Label(root, text = 'eps', width = 10)
h4.grid(row = 1, column = 4)
epsh = Entry(root, width = 10)
epsh.grid(row= 2, column = 4)
h5 = Label(root, text = 'NMax', width = 10)
h5.grid(row = 1, column = 5)
nmaxh = Entry(root, width = 10)
nmaxh.grid(row= 2, column = 5)
h5e = Label(root, text = 'Коды ошибки:')
h5e.grid(row = 1, column = 6)
h5e = Label(root, text = '0 - все хорошо')
h5e.grid(row = 2, column = 6)
h5e = Label(root, text = '1 - превышение итераций')
h5e.grid(row = 3, column = 6)
start_butt = Button(root, text = 'Start',command = starto)
start_butt.grid(row = 3, column = 1)
graph_butt = Button(root, text = 'График',command = show_graph)
graph_butt.grid(row = 3, column = 2)

h6 = Label(root, text = '№', width = 10,borderwidth=2, relief="solid")
h6.grid(row = 4, column = 1)
h7 = Label(root, text = 'Интервал', width = 10,borderwidth=2, relief="solid")
h7.grid(row = 4, column = 2)
h8 = Label(root, text = 'Зн. корня', width = 10,borderwidth=2, relief="solid")
h8.grid(row = 4, column = 3)
h9 = Label(root, text = 'Зн. ф-ции', width = 10,borderwidth=2, relief="solid")
h9.grid(row = 4, column =4)
h11 = Label(root, text = 'Итерации', width = 10,borderwidth=2, relief="solid")
h11.grid(row = 4, column = 5)
h12 = Label(root, text = 'Код ошибки', width = 10,borderwidth=2, relief="solid")
h12.grid(row = 4, column = 6)
root.mainloop()
