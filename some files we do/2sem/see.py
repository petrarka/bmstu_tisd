# Задача:
# 1. При помощи метода СЕКУЩИХ найти все приближенные корни функции на отрезке
#   [a,b] с шагом "h" и точностью "eps".
# 2. Сделать графическую интерпретацию решения:
#   на графике отметить корни и ЭКСТРЕМУМЫ.
# Функция: f(x) = x^3+x^2-3
# 
# Переменные:
# sva,svb,svh,sveps,sviter - переменные ввода
# Ea,Eb,Eh,Eeps,Eiter - графические переменные (Entry)
# a,b,h,eps,iter - рабочие переменные
# A,a1,b1, - рабочие переменные
# rg,Px,Py,fmin,fmax - рабочие переменные
# Listbox1,Listbox2,Listbox3,Listbox4,Listbox5,Listbox6 - графические переменные
# Label1, Label2, Label3, LabelEh, LabelEeps, LabelNumIter,
#   LabelNo, LabelElemInter, LabelMeanOfRoot, LabelMeanOfFunc,
#   LabelNumOfIter, LabelCodeError - графические переменные
#
from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root['bg'] = 'LightBlue'
root.geometry('700x500')
root.title('Метод секущих')

M = Menu(root)
root.config(menu = M)
MainMenu = Menu(M)
CodeError = Menu(M)
M.add_cascade(label = 'Меню', menu = MainMenu)
M.add_cascade(label = 'Код ошибки', menu = CodeError)

sva = StringVar()
svb = StringVar()
svh = StringVar()
sveps = StringVar()
sviter = StringVar()

Ea = Entry(root,width = 5,font = 'Vernada 12 bold', bd = 2,textvariable = sva)
Eb = Entry(root,width = 5,font = 'Vernada 12 bold', bd = 2,textvariable = svb)
Eh = Entry(root,width = 5,font = 'Vernada 12 bold', bd = 2,textvariable = svh)
Eeps = Entry(root,width = 10,font = 'Vernada 12 bold',bd = 2,
             textvariable = sveps)
Eiter = Entry(root,width = 5,font = 'Vernada 12 bold',bd = 2,
             textvariable = sviter)

Scrollbar = Scrollbar(root)
Scrollbar.pack(side = RIGHT, fill = Y)

#-------------------------------------------------------------------------------
def IsNum(S): # Проверка на целое число
    F = False
    if S:
        if S[0] == '-':
            S = S[1:]
        for i in S:
            if not i.isdigit():
                return False
        return True
    else:
        return False

def IsNumWithPoint(S): # Проверка на дробное число
    F = False
    if S[0] == '-':
        S = S[1:]
    for i in S:
        if not i.isdigit():
            if i == '.':
                if F:
                    return(False)
                else:
                    F = True
            else:
                return(False)
    return(True)

def Func(x): # Вычисление функции f(x) = x*x*x - 4*x*x +5

    return x**3 - 4*x**2 - x + 5
    

def Compute():
    ClearListbox()
    
    a = sva.get()
    b = svb.get()
    h = svh.get()
    eps = sveps.get()
    itr = sviter.get()
    if a and b and h and eps and itr \
       and IsNumWithPoint(a) and IsNumWithPoint(b) and IsNumWithPoint(h) \
       and IsNumWithPoint(eps) and IsNum(itr):
        
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        itr = int(itr)
        eps1 = h/10
        
        if a > b:
            messagebox.showerror('Ошибка','Неверный ввод! \n         a > b!')
        elif a == b:
            messagebox.showerror('Ошибка','Неверный ввод! \n         a = b!')
        else:
            # Уточнение корней методом секущих
            prev = a-h
            for i in range(round((b-a)/h+0.5)):
                a1 = a + h * i
                b1 = a + h * (i+1)
                A = Method(a1,b1,eps,itr)
                if a1 - eps1 < A[0] <= b1 + eps1 and abs(A[0] - prev) > eps1:
                    Listbox1.insert(END,i+1)
                    Listbox2.insert(END,'['+ str(a1) +' ; '+ str(b1)+']')
                    Listbox3.insert(END, '{:.5f}'.format(A[0]))
                    Listbox4.insert(END,'{:.0e}'.format(Func(A[0])))
                    Listbox5.insert(END,A[1])
                    prev = A[0]
                    
                    if A[1] <= itr:
                        Listbox6.insert(0,'-')
                    else:
                        Listbox6.insert(0,1)
            if Listbox1.size() == 0:
                messagebox.showerror('Нет корней',
                                     'Нет корней на заданном интервале')
            
    else:
        messagebox.showerror('Ошибка','Неверный ввод!')
    
    print()

def Method(a,b,eps,itr): # Метод секущих
    x1 = (a + b) / 2
    x2 = a + (b-a)/3
    x3 = x2
    t = 0
    while abs(Func(x3)) > eps and (t <= itr):
        #print(x1, x2)
        #print(Func(x1), Func(x2))
        x3 = x2 - ((x2 - x1) / (Func(x2)- Func(x1))) * Func(x2)
        x1 = x2
        x2 = x3
        t += 1
        #print(a,b,x1,x2,x3)
    return (x3,t)

def PlottingGraphic():
    a = sva.get()
    b = svb.get()
    h = svh.get()
    eps = sveps.get()
    itr = sviter.get()
    
    a = float(a)
    b = float(b)
    h = float(h)
    eps = float(eps)
    itr = int(itr)
    eps1 = h/10

    rg = round((b-a)/h + 0.5)
    Px = []
    Py = []
    

    x = np.arange(a,b,0.01)
    vf = np.vectorize(Func)
    y = vf(x)
    plt.plot(x,y)
    plt.grid()
    
    fmin = np.min(y)
    fmax = np.max(y)
    
    for i in range(len(x)):
        if abs(y[i] - fmin) < eps or abs(y[i] - fmax) < eps:
            Px.append(x[i])
            Py.append(y[i])
    plt.scatter(Px,Py, color = 'g')


    Px = []
    Py = []
    prev = a-h
##    for i in range(rg):
##        a1 = a + h * i
##        b1 = a + h * (i+1)
##        A = Method(a1,b1,eps,itr)
##        if a1 - eps1 < A[0] <= b1 + eps1 and abs(A[0] - prev) > eps1:
##            Px.append(A[0])
##            Py.append(Func(A[0]))
##            prev = A[0]
##    plt.scatter(Px,Py, color = 'r')


    plt.ylim(fmin-0.05*abs(fmax-fmin),fmax+0.05*abs(fmax-fmin))
    plt.xlim(a-0.05*abs(b-a),b+0.05*abs(b-a))
    
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False) 
       
    plt.show()

def ClearFields(): # Очистка полей ввода
    Ea.delete(0,END)
    Eb.delete(0,END)
    Eh.delete(0,END)
    Eeps.delete(0,END)
    Eiter.delete(0,END)
    Listbox1.delete(0,END)
    Listbox2.delete(0,END)
    Listbox3.delete(0,END)
    Listbox4.delete(0,END)
    Listbox5.delete(0,END)
    Listbox6.delete(0,END)

def ClearListbox(): # Очистка полей вывода
    Listbox1.delete(0,END)
    Listbox2.delete(0,END)
    Listbox3.delete(0,END)
    Listbox4.delete(0,END)
    Listbox5.delete(0,END)
    Listbox6.delete(0,END)

def OnMouseWheel(event): # Прокрутка окна
    Listbox1.yview("scroll", -event.delta // 10,"units")
    Listbox2.yview("scroll", -event.delta // 10,"units")
    Listbox3.yview("scroll", -event.delta // 10,"units")
    Listbox4.yview("scroll", -event.delta // 10,"units")
    Listbox5.yview("scroll", -event.delta // 10,"units")
    Listbox6.yview("scroll", -event.delta // 10,"units")
    return "break"

def Err1():
    print()
def Err2():
    print()

#-------------------------------------------------------------------------------
MainMenu.add_command(label = 'Очистить поля',command = ClearFields)
CodeError.add_command(label = '1 - Превышено кол-во интервалов',command = Err1)
#CodeError.add_command(label = '2 - ',command = Err2)


LabNameLabel = Label(root, text = 'Метод секущих',
                fg='DarkBlue',font = 'Verdana 14 italic bold')
LabelEab = Label(root, text = 'Введите границы отрезка [a,b]:',
                fg='DarkBlue',font = 'Vernada 12 bold')

Label1 = Label(root, text = '[', font = 'Vernada 14 bold')
Label2 = Label(root, text = ';', font = 'Vernada 14 bold')
Label3 = Label(root, text = ']', font = 'Vernada 14 bold')

LabelEh = Label(root, text = 'Введите шаг для разбиения на отрезки (h):',
                fg='DarkBlue',font = 'Vernada 12 bold')
LabelEeps = Label(root, text = 'Введите точность вычисления (eps):',
                fg='DarkBlue',font = 'Vernada 12 bold')
LabelNumIter = Label(root, text = 'Введите допустимое кол-во итераций:',
                fg='DarkBlue',font = 'Vernada 12 bold')

LabelNo = Label(root, text = '№ интервала',
                fg='DarkBlue',font = 'Vernada 9')
LabelElemInter = Label(root, text = 'Элементарный \n интервал',
                fg='DarkBlue',font = 'Vernada 9')
LabelMeanOfRoot = Label(root, text = 'Значение \n корня',
                fg='DarkBlue',font = 'Vernada 9')
LabelMeanOfFunc = Label(root, text = 'Значение функции \n от корня',
                fg='DarkBlue',font = 'Vernada 9')
LabelNumOfIter = Label(root, text = 'Кол-во \n итераций',
                fg='DarkBlue',font = 'Vernada 9')
LabelCodeError = Label(root, text = 'Код \n ошибки',
                fg='DarkBlue',font = 'Vernada 9')


Listbox1 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 15)
Listbox2 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 15)
Listbox3 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 17)
Listbox4 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 18)
Listbox5 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 19)
Listbox6 = Listbox(root, yscrollcommand = Scrollbar.set,
                  height = 14,width = 15)

Listbox1.bind("<MouseWheel>", OnMouseWheel)
Listbox2.bind("<MouseWheel>", OnMouseWheel)
Listbox3.bind("<MouseWheel>", OnMouseWheel)
Listbox4.bind("<MouseWheel>", OnMouseWheel)
Listbox5.bind("<MouseWheel>", OnMouseWheel)
Listbox6.bind("<MouseWheel>", OnMouseWheel)


ButtonCalc = Button(root,text = 'Расчитать',width = 15,height = 1,
                   font = 'Vernada 12 bold',bg = 'DarkBlue',fg = 'white',
                   command = Compute)
ButtonPlot = Button(root,text = 'График',width = 15,height = 1,
                   font = 'Vernada 12 bold',bg = 'DarkBlue',fg = 'white',
                   command = PlottingGraphic)

# Смена цветов
LabNameLabel['bg'] = 'LightBlue'
LabelEab['bg'] = 'LightBlue'
Label1['bg'] = 'LightBlue'
Label2['bg'] = 'LightBlue'
Label3['bg'] = 'LightBlue'
LabelEh['bg'] = 'LightBlue'
LabelEeps['bg'] = 'LightBlue'
LabelNumIter['bg'] = 'LightBlue'
LabelNo['bg'] = 'LightBlue'
LabelElemInter['bg'] = 'LightBlue'
LabelMeanOfRoot['bg'] = 'LightBlue'
LabelMeanOfFunc['bg'] = 'LightBlue'
LabelNumOfIter['bg'] = 'LightBlue'
LabelCodeError['bg'] = 'LightBlue'

# Размещение элементов на виджете
LabNameLabel.place(x = 270,y = 20)

LabelEab.place(x = 20,y = 70)
Ea.place(x = 292,y = 71)
Eb.place(x = 360,y = 71)

Label1.place(x = 278,y = 68)
Label2.place(x = 345,y = 68)
Label3.place(x = 412,y = 68)

LabelEh.place(x = 20,y = 100)
Eh.place(x = 370,y = 100)

LabelEeps.place(x = 20,y = 130)
Eeps.place(x = 325,y = 130)

LabelNumIter.place(x = 20,y = 160)
Eiter.place(x = 370,y = 160)

LabelNo.place(x = 20,y = 220)
LabelElemInter.place(x = 120,y = 215)
LabelMeanOfRoot.place(x = 240,y = 215)
LabelMeanOfFunc.place(x = 330,y = 215)
LabelNumOfIter.place(x = 477,y = 215)
LabelCodeError.place(x = 590,y = 215)

Listbox1.place(x = 18, y = 250)
Listbox2.place(x = 118, y = 250)
Listbox3.place(x = 218, y = 250)
Listbox4.place(x = 330, y = 250)
Listbox5.place(x = 448, y = 250)
Listbox6.place(x = 572, y = 250)


##Scrollbar.config(command = Listbox1.yview)
##Scrollbar.config(command = Listbox2.yview)
##Scrollbar.config(command = Listbox3.yview)
##Scrollbar.config(command = Listbox4.yview)
##Scrollbar.config(command = Listbox5.yview)
##Scrollbar.config(command = Listbox6.yview)



ButtonCalc.place(x = 480,y = 110)
ButtonPlot.place(x = 480,y = 150)

root.mainloop()
