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
    return sin(x)
## Метод
def secant(f, x1, x0, eps, nmax):
   n = 0
   while n <= nmax:
      x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
      if abs(x2-x1) < eps:
         return x2,n
      else:
         x0 = x1
         x1 = x2
      n += 1
   return x2,-2

## Разбиение на участки      
def tabul(a,b,step,eps,nmax):
   t = a + step
   ans = []
   itter = []
   inter = []
   while a < b:
      if f(a) * f(t) <= 0:
         x,i = secant(f,a,t,eps,nmax)
         if i == -2:
            ss = t
            e = '+'
            if t > b:
               ss = b
            if x > ss:
                x = '-'
                e = '-'
                s = '-'
            s = '[' + str(a) + ';' + str(ss) + ']'
            ans.append(x)
            itter.append(e)
            inter.append(s)
         elif (a<=x<=t):
            ss = t
            if t > b:
               ss = b
            if x > ss:
                x = '-'
                s = '-'
                i = '-'
            if len(ans) != 0 and x == ans[len(ans)-1]:
                x = '-'
                s = '-'
                i = '-'
            s = '[' + str(a) + ';' + str(ss) + ']'
            itter.append(i)
            ans.append(x)
            inter.append(s)
         else:
            ans.append('-')
            itter.append('-')
            inter.append('-')
      else:
          ans.append('-')
          itter.append('-')
          inter.append('-')
      a = t
      t += step
   return ans,itter,inter

## Построение таблицы
def table(ans, itter, inter):
   it = 0
   for i in range(len(ans)):
      n = i +5
      if itter[i] == '+':
         Listbox1.insert(END,it+1)
         Listbox2.insert(END,inter[i])
         Listbox3.insert(END, '----')
         Listbox4.insert(END, '----')
         Listbox5.insert(END, '----')
         Listbox6.insert(END, '1')
         it += 1
      elif itter[i] != '-':
         s = str('{:.0e}'.format(f(ans[i])))
         an = str("%.6f" % ans[i])
         Listbox1.insert(END,it+1)
         Listbox2.insert(END,inter[i])
         Listbox3.insert(END,an)
         Listbox4.insert(END,s)
         Listbox5.insert(END,str(itter[i]))
         Listbox6.insert(END,'0')
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

## Построение графика
def show_graph():
    a = float(left.get())
    b = float(right.get())
    step = float(steph.get())
    nmax = int(nmaxh.get())
    eps = float(epsh.get())
    
    Px = []
    Py = []
    x = np.arange(a,b,0.01)
    vf = np.vectorize(f)
    y = vf(x)
    plt.plot(x,y)
    plt.grid(True)

    fmin = np.min(y)
    fmax = np.max(y)
                  
    plt.ylim(fmin,fmax)
    plt.xlim(a,b)
    ans, itter, inter = tabul(a,b,step,eps,nmax)
    for i in range(len(ans)):
      if itter[i] == '+':
         Px.append(ans[i])
         Py.append(f(ans[i]))
      elif itter[i] != '-':
         Px.append(ans[i])
         Py.append(f(ans[i]))
         
    plt.scatter(Px,Py, color = 'r')
    for i in range(len(y)):
        if fabs((y[i] - fmin)) <= 0.001:
            plt.scatter(x[i],f(x[i]), color = 'b')
        if fabs((y[i] - fmax)) <= 0.001:
            plt.scatter(x[i],f(x[i]), color = 'g')

    if fabs((f(x[len(x)-1] + 0.01) - fmin)) <= 0.001:
        plt.scatter((x[len(x)-1] + 0.01),(f(x[len(x)-1] + 0.01)), color = 'b')
    if fabs((f(x[len(x)-1] + 0.01) - fmax)) <= 0.001:
        plt.scatter((x[len(x)-1] + 0.01),(f(x[len(x)-1] + 0.01)), color = 'g')
    plt.show()

def scroll(event): # Прокрутка окна
    Listbox1.yview("scroll", -event.delta // 10,"units")
    Listbox2.yview("scroll", -event.delta // 10,"units")
    Listbox3.yview("scroll", -event.delta // 10,"units")
    Listbox4.yview("scroll", -event.delta // 10,"units")
    Listbox5.yview("scroll", -event.delta // 10,"units")
    Listbox6.yview("scroll", -event.delta // 10,"units")

def clslistbox(): # Очистка полей вывода
    Listbox1.delete(0,END)
    Listbox2.delete(0,END)
    Listbox3.delete(0,END)
    Listbox4.delete(0,END)
    Listbox5.delete(0,END)
    Listbox6.delete(0,END)

## Запуск
def starto():
    clslistbox()
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
    table(ans, itter, inter)


root = Tk()
root.geometry('800x300')
root.title("График функции")

Scrollbar = Scrollbar(root)
Scrollbar.pack(side = RIGHT, fill = Y)

Listbox1 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 15)
Listbox2 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 15)
Listbox3 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 17)
Listbox4 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 18)
Listbox5 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 19)
Listbox6 = Listbox(root, yscrollcommand = Scrollbar.set, height = 14,width = 15)
Listbox1.bind("<MouseWheel>", scroll)
Listbox2.bind("<MouseWheel>", scroll)
Listbox3.bind("<MouseWheel>", scroll)
Listbox4.bind("<MouseWheel>", scroll)
Listbox5.bind("<MouseWheel>", scroll)
Listbox6.bind("<MouseWheel>", scroll)
Listbox1.place(x = 18, y = 120)
Listbox2.place(x = 118, y = 120)
Listbox3.place(x = 218, y = 120)
Listbox4.place(x = 328, y = 120)
Listbox5.place(x = 448, y = 120)
Listbox6.place(x = 548, y = 120)
    
h1 = Label(root, text = 'От', width = 15)
h1.place(x = 18, y = 10)
left = Entry(root, width = 15)
left.place(x = 18, y = 30)

h2 = Label(root, text = 'До', width = 17)
h2.place(x = 118, y = 10)
right = Entry(root, width = 17)
right.place(x = 118, y = 30)

h3 = Label(root, text = 'Шаг', width = 18)
h3.place(x = 218, y = 10)
steph = Entry(root, width = 18)
steph.place(x = 218, y = 30)

h4 = Label(root, text = 'eps', width = 19)
h4.place(x = 328, y = 10)
epsh = Entry(root, width = 19)
epsh.place(x = 328, y = 30)

h5 = Label(root, text = 'NMax', width = 15)
h5.place(x = 448, y = 10)
nmaxh = Entry(root, width = 15)
nmaxh.place(x = 448, y = 30)

h5e = Label(root, text = ' Коды ошибки:')
h5e.place(x = 548, y = 10)
h5e = Label(root, text = '0 - все хорошо')
h5e.place(x = 548, y = 30)
h5e = Label(root, text = '1 - превышение итераций')
h5e.place(x = 548, y = 50)

start_butt = Button(root, text = 'Start',command = starto, width = 10)
start_butt.place(x = 18, y = 60)
graph_butt = Button(root, text = 'График',command = show_graph, width = 10)
graph_butt.place(x = 118, y = 60)

h6 = Label(root, text = '№', width = 13,borderwidth=2, relief="solid")
h6.place(x = 18, y = 90)
h7 = Label(root, text = 'Интервал', width = 13,borderwidth=2, relief="solid")
h7.place(x = 118, y = 90)
h8 = Label(root, text = 'Зн. корня', width = 15,borderwidth=2, relief="solid")
h8.place(x = 218, y = 90)
h9 = Label(root, text = 'Зн. ф-ции', width = 15,borderwidth=2, relief="solid")
h9.place(x = 330, y = 90)
h11 = Label(root, text = 'Итерации', width = 13,borderwidth=2, relief="solid")
h11.place(x = 448, y = 90)
h12 = Label(root, text = 'Код ошибки', width = 13,borderwidth=2, relief="solid")
h12.place(x = 550, y = 90)
root.mainloop()
