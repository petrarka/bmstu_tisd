#Программа для нахождения корней методом Ньютона и построения графиков
#Выполнил: Зейналов Зейнал ИУ7-11Б
#a - левый конец отрезка  b - правый конец отрезка  h - шаг  eps -точность  
# N - кол-во итерраций
# flag - логическая переменная для проверки на наличие "-" в числе
# flag - логическая переменная для проверки на наличие "." в числе
# count - логическая переменная для выяснения кол-ва
# mamory - позиция точки в числе
# massive - массив из значений элементарных отрезков
# mini_intervals - мини интервалы от а до b с шагом h
# mass - промежуточный мини инетервалы
# check_massive - массив из интервалов , содержащих 1 корень
# peregib_check_massive - массив, содержащий отрезки , где есть точки перегиба
# base - массив из элементов, взятых в качестве приближенного значения
# roots_2 - массив из элементов, взятых в качестве приближенного значения
# для точки перегиба
# massiveN - массив из количеств итерраций
# error - массив из кодов ошибки
# results - массив значений функции
# peregib - массив значений точек перегиба
# f_diff - частное функции и производной для нахождения корней
# n1 - переменная для подсчета кол-ва итерраций
# f_diff1 - частное функции и производной для нахождения точек перегиба
# 
# 
# 
# ТЕСТОВЫЕ ДАННЫЕ!!!!!!!!!
#
#exp(x)-x-2  exp(x)-1  exp(x)   x1 = -1,84 x2 = 1,14
#x**3+3*x+2.2  3*x**2+3  6*x  x1 = -0.644
#x**3+4*x**2-3 3*x**2+8*x 6*x+8  (-3.79154247392,0.791831,-1)
#x**3+x-3    3*x**2+1   6*x  x = 1.213...
#x**5-5*x+2*x**2  5*x**4-5+4*x  20*x**3+4  60*x**2
#x**2+x**3+x**7-x**8  2*x+3*x**2+7*x**6-8*x**7  2+6*x+42*x**5-56*x**6  
#x**4+4*x**3-6*x  4*x**3+12*x**2-6  12*x**2+24*x  24*x+24
#коды ошибок 0 1 


from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return(sin(x))
def diff(x):
    return(cos(x))
def diff2(x):
    return(-sin(x))
def diff3(x):
    return(-cos(x))

def main():
    # Ввод элементов с проверкой на правильность ввода
    global results
    print("------begin------")
    a = ent2.get()
    
    count = 0
    flag = False
    flag1 = False
    if a[0] == '-':
        flag1 = True
        a = a[1:]
    for i in range(len(a)):
        if a[i] =='.':
            flag = True
            memory = i
            count+=1
    if flag == True and count == 1:
        a1 = a[:memory]
        a2 = a[memory+1:]
        if a1.isdigit() and a2.isdigit():
            a = float(a)
        else:
            messagebox.showinfo('Внимание','Неверное значение левого конца \
    отрезка')
            return 0;
            
    else:
        if a.isdigit():
            a = float(a)
        else:
            messagebox.showinfo('Внимание','Неверное значение левого конца \
    отрезка')
            return 0;
    if flag1 ==True:
        a*=-1
    
    
    b = ent3.get()

    count = 0
    flag = False
    flag1 = False
    if b[0] == '-':
        flag1 = True
        b = b[1:]
    for i in range(len(b)):
        if b[i] =='.':
            flag = True
            memory = i
            count+=1
    if flag == True and count == 1:
        b1 = b[:memory]
        b2 = b[memory+1:]
        if b1.isdigit() and b2.isdigit():
            b = float(b)
        else:
            messagebox.showinfo('Внимание','Неверное значение правого конца \
    отрезка')
            return 0;
            
    else:
        if b.isdigit():
            b = float(b)
        else:
            messagebox.showinfo('Внимание','Неверное значение правого конца \
    отрезка')
            return 0;
    if flag1 ==True:
        b*=-1

    
    h = ent4.get()
    if h == '' or h[0] == '-' or h == '0':
        messagebox.showinfo('Внимание','Шаг должен быть положительным числом')
        return 0;
    else:
        if h.isdigit():
            h = float(h)
        elif h[0].isdigit() and h[1] == '.' and h[2:].isdigit() and h[2:]!='0':
            h = float(h)
        
        else:
            messagebox.showinfo('Внимание','Неверное значение шага')
            return 0;

        
    eps = ent5.get()
    if eps =='' or eps[0] == '-' :
        messagebox.showinfo('Внимание','Эпсилон не может быть отрицательным')
        return 0;
    else:
        if eps[0] == '0' and eps[1] == '.' and eps[2:].isdigit():
            eps = float(eps)
            if 0<eps and eps<1:
                print('ok')
            else:
                messagebox.showinfo('Внимание','Эписолон больше нуля и \
меньше единицы')
                return 0;
        else:
            messagebox.showinfo('Внимание','Неверное значение Эпсилон')
            return 0;
        
        
    N = ent6.get()
    if N =='' or N[0] == '-':
        messagebox.showinfo('Внимание','Кол-во итерраций больше нуля')
        return 0;
    else:
        if N.isdigit() :
            N = int(N)
        else:
            messagebox.showinfo('Внимание','Неверное значение кол-ва итерраций')
            return 0;
    

    error = []
    massive = []
    print(a,b,eps,h,N)
    i = a
    # создание массива из элементов отрезка
    while i<=b:
        massive.append(i)
        i+=h
    print(massive)

    mini_intervals = []
    #создание элементарных отрезков
    while a+h<b:
        mass = []
        mass.append(a)
        a+=h
        a = str(a)
        a = a[:6]
        a = float(a)
        mass.append(a)
        mini_intervals.append(mass)
    else:
        mass = []
        mass.append(a)
        a = b
        mass.append(a)
        mini_intervals.append(mass)
    print('мини интервалы ',mini_intervals)
    check_massive = []
    results = []
    count = 0
    # Поиск элементарных отрезков, содержащих 1 корень
    for i in range(len(mini_intervals)):
        if f(mini_intervals[i][0])*f(mini_intervals[i][1]) < 0:
            check_massive.append(mini_intervals[i])
         
        if i == 0 and f(mini_intervals[i][0]) == 0:
                check_massive.append(mini_intervals[0])
##        elif i == 1 and f(mini_intervals[i][1]) == 0:
##            check_massive.append(mini_intervals[1])
        elif f(mini_intervals[i][0])==0 and f(mini_intervals[i-1][1])==0:
                check_massive.append(mini_intervals[i])
        elif i == len(mini_intervals)-1 and f(mini_intervals[i][1]) == 0:
                check_massive.append(mini_intervals[i])
        
        

            
                
    print("корни",check_massive)
    #check_massive -массив отрезков , содержащих корни
    base = []
    #Посик приближенного значения в отрезках для уточнения корня
##    for i in range(len(check_massive)):
####        Здесь правильно выбирать приближенные значения !!!!!
##        if diff(check_massive[i][0]) != 0 and diff(check_massive[i][1])!=0 :
##            if f(check_massive[i][0]) == 0:
##                base.append(check_massive[i][0])
##            elif f(check_massive[i][1]) == 0:
##                base.append(check_massive[i][1])
##            else:
##                base.append(check_massive[i][1])
####            base.append(check_massive[i][0])
##                
##        elif diff(check_massive[i][0]) != 0 and diff(check_massive[i][1])==0:
##            base.append(check_massive[i][0])
##        elif diff(check_massive[i][0]) == 0 and diff(check_massive[i][1])!=0:
##            base.append(check_massive[i][1])
##                
##            break
##        else:
##            continue
##                    
    print("приближенные значения: ",base)
    massiveN = []
    #Метод Ньютона для уточнения корней
    for i in range(len(check_massive)):
        flag = True
        for j in range(len(check_massive[i])):
            if flag == False:
                break
            if diff(check_massive[i][j]) == 0:
                continue
            f_diff = f(check_massive[i][j]) / (diff(check_massive[i][j]))
            x = check_massive[i][j]
            n1 = 1
            while abs(f_diff) > eps and n1 < N:
                    
                f_diff = str(f_diff)

                f_diff = f_diff[:14]
                    
                f_diff = float(f_diff)
                    
                x = x-f_diff
                f_diff = f(x) / (diff(x))
                n1+=1
            print("x is 1\n", x)
            if check_massive[i][0] <= x and x <= check_massive[i][1] and n1<N:    
                massiveN.append(n1)
                results.append(x)
                error.append(0)
                flag = False
            if j == 1 and flag == True:
                if check_massive[i][0] <= x and x <= check_massive[i][1] and n1>=N:
                    massiveN.append(n1)
                    results.append('none')
                    error.append(1)
                elif check_massive[i][0] > x or x > check_massive[i][1]:
                    massiveN.append(n1)
                    print(x,"здесь он")
                    error.append(2)
                    results.append('none')
                

   
        
    
    print("корни :",results)
    print("итеррации: ",massiveN)

    

    listbox1.delete(0,END)
    listbox2.delete(0,END)
    listbox3.delete(0,END)
    listbox4.delete(0,END)
    listbox5.delete(0,END)
    listbox6.delete(0,END)
    
    # Заполнение Таблицы значений
    for i in range(len(results)):
        if results[i] != 'none':
            listbox1.insert(END,"{:^15}".format(str(i+1)))
            listbox2.insert(END,"{:^30}".format(str(check_massive[i])))
            listbox3.insert(END,"{:^40.5f}".format(results[i]))
            listbox4.insert(END,"{:^40.0e}".format(f(results[i])))
            listbox5.insert(END,"{:^26}".format(str(massiveN[i])))
            listbox6.insert(END,"{:^30}".format(str(error[i])))
        else:
            listbox1.insert(END,"{:^15}".format(str(i+1)))
            listbox2.insert(END,"{:^30}".format(str(check_massive[i])))
            listbox3.insert(END,"{:^50}".format('-'))
            listbox4.insert(END,"{:^50}".format('-'))
            listbox5.insert(END,"{:^30}".format('-'))
            listbox6.insert(END,"{:^30}".format(str(error[i])))
    if check_massive == []:
        messagebox.showinfo('Внимание','Нет корней на заданном отрезке')

# Построение графика
def graph():
    

    a = ent2.get()
    b = ent3.get()
    h = ent4.get()
    eps = ent5.get()
    eps= float(eps)
    a = float (a)
    b = float (b)
    h = float (h)
    h = h/10
    left = a
    right = b
    mini_intervalsp = []
    while a<b:
        massp = []
        massp.append(a)
        a+=1
        massp.append(a)
        mini_intervalsp.append(massp)
    print("Intervals for peregib: ",mini_intervalsp)
    peregib_check_massive = []
    roots_2 = []
    for i in range(len(mini_intervalsp)):
        if diff2(mini_intervalsp[i][0])*diff2(mini_intervalsp[i][1])<=0:
                peregib_check_massive.append(mini_intervalsp[i])
    #Поиск приближенного значени для нахождения точки перегиба
    for i in range(len(peregib_check_massive)):
        roots_2.append(peregib_check_massive[i][1])

    #нахождение точки перегиба        
    peregib = []
    for i in roots_2:
        if diff3(i) == 0:
            continue
        f_diff1 = diff2(i) / diff3(i)
        x = i
        n1 = 0
        while abs(f_diff1) > eps :
            x = x - f_diff1
            
            f_diff1 = diff2(x) / diff3(x)
            n1+=1
        peregib.append(x)
    print("точки перегиба",peregib)
    
    

    X = np.arange(left, right, h)
    Y = np.empty(0)
    for i in range(len(X)):
        Y = np.append(Y, f(X[i]))
    
    plt.plot(X, Y)
    plt.grid(True)

    plt.ylim(-7, 7)
    plt.xlim(left, right, h)
    for i in range(len(peregib)):
        plt.plot(peregib[i], f(peregib[i]), 'yo')
        
    for j in range(len(results)):
        if results[j] == 'none':
            continue
        else:
            plt.plot(results[j], f(results[j]), 'ro')
            
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()
            
    
#создание окна
root = Tk()
root.title('Нахождение корней методом касательных')
root.geometry('800x680')
root.resizable(width=False,height=False)
root.configure(bg = '#e3ecf7')



l = Label(root,text=('Введите отрезок, на котором будут искаться корни:\
[        :         ] ')
          ,bg='#e3ecf7',font = "Arial 14").place(x=20,y=30)

l = Label(root,text=('Введите шаг для разбиения на элементарные отрезки: ')
          ,bg='#e3ecf7',font = "Arial 14").place(x=20,y=60)

l = Label(root,text=('Введите точность (эпсилон) для вычисления корней: ')
          ,bg='#e3ecf7',font = "Arial 14").place(x=20,y=90)

l = Label(root,text=('Введите допустимое кол-во итерраций: ')
          ,bg='#e3ecf7',font = "Arial 14").place(x=20,y=120)

l = Label(root,text=('Номер: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=10,y=220)
l = Label(root,text=('Элементарный \n отрезок: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=90,y=220)
l = Label(root,text=('Значение \n корня: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=230,y=220)
l = Label(root,text=('Значение \n функции: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=380,y=220)
l = Label(root,text=('Количество \n иттераций: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=530,y=220)
l = Label(root,text=('Код ошибки: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=640,y=220)

l = Label(root,text=('Коды ошибок: ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=20,y=590)

l = Label(root,text=('0 - Нахождение прошло без ошибок ')
          ,bg='#e3ecf7',font = "Arial 10").place(x=20,y=610)

l = Label(root,text=('1 - За N итерраций не удалось найти корень')
          ,bg='#e3ecf7',font = "Arial 10").place(x=20,y=630)

l = Label(root,text=('2 - Корень не удалось найти (Вычисленный корень лежит вне \
элементарного отрезка)')
          ,bg='#e3ecf7',font = "Arial 10").place(x=20,y=650)



ent2 = Entry(width = 5)
ent2.place(x=485,y=36)

ent3 = Entry(width = 5)
ent3.place(x=530,y=36)

ent4 = Entry(width = 5)
ent4.place(x=510,y=66)

ent5 = Entry(width = 5)
ent5.place(x=510,y=96)

ent6 = Entry(width = 5)
ent6.place(x=510,y=126)

but2 = Button(root,text='Рассчитать',command=main,width=8,height=1
             ,bg = '#d6e1ee',fg='black')

but2.place(x=200,y=180)


but3 = Button(root,text='График',command = graph,width=8,height=1
             ,bg = '#d6e1ee',fg='black')

but3.place(x=300,y=180)

scrollbar = Scrollbar(root)
listbox1 = Listbox(yscrollcommand=scrollbar.set,
                   selectmode=EXTENDED,height=20,width=9)
listbox1.place(x =10,y=260)
scrollbar.config(command=listbox1.yview)

listbox2 = Listbox(height=20,width=20)
listbox2.place(x =65,y=260)

listbox3 = Listbox(height=20,width=26)
listbox3.place(x =188,y=260)

listbox4 = Listbox(height=20,width=27)
listbox4.place(x =348,y=260)

listbox5 = Listbox(height=20,width=17)
listbox5.place(x =514,y=260)

listbox6 = Listbox(height=20,width=20)
listbox6.place(x =620,y=260)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command = listbox1.yview)
scrollbar.config(command = listbox2.yview)
scrollbar.config(command = listbox3.yview)


root.mainloop()
                   

##from math import *
##def f(x):
##    return sin(x)
##
##def f1(x):
##    return cos(x)
##
##def new(a,b,f,f1,eps):
##    it = 0
##    while True:
##        print(a)
##        x1 = a - (f(a)/f1(a))
##        if abs(x1-a) < eps:
##            print('e',x1)
##            print('t',it)
##            return x1,it
##        a = x1
##        it += 1
##        print(a)
##    print('noo')
##a = 5
##b = 8
##eps = 0.0001
##x1,t1 = new(a,b,f,f1,eps)
##x2,t2 = new(b,a,f,f1,eps)
##if a<x1<b:
##    print(x1, t1)
##elif a<x2<b:
##    print(x2,t2)
##else:
##    print("nooo")
##    print(x1,x2)
