### Калькулятор для перевода в троичную систему счисления и обратно
###                                         Сангинов Азамат ИУ7-21Б

### butt0, butt1,...,butt9 - кнопки с цифрами,
### buttmin - кнопка минуса
### point - кнопка точки
### clear_alll, clear_anss - очистка полей
### equal1, equal2 - перевод в другую систему
### equation, tot - поля с числами
### equa - вводимое число
### num - число для перевода
### tern_num, dec_num - троичное и десятичное числа после перевода

from tkinter import *

# Функция перевода в троичную целой части
def transint(num):
   f = 0
   num = int(num)
   tern_num = ''
   if num<0:
      num = -num
      f = 1
   if num == 0:
      return 0
   while num > 0:
      remainder = num % 3
      num //= 3
      tern_num += str(remainder)
   if f:
      tern_num = '-' + tern_num[::-1]
   else:
      tern_num = tern_num[::-1]
   return tern_num

# Функция перевода в троичную дробной части
def transfract(num):
   k = 6
   real_num = ''
   num = float(num)
   p = num
   while k > 0:
      p*=3
      real_num += str(int(p))
      if p > 1:
         p = p - int(p)
      k -= 1
   return real_num

#Функция перевода из троичной целой части
def transint_rev(num):
   f = 0
   numlen = len(num)-1
   dec_num = 0
   if int(num)<0:
      f = 1
      num = num[1::]
   for i in range(numlen,-1,-1):
      dec_num += 3**i * int(num[numlen-i])
   return dec_num

# Функция перевода из троичной дробной части
def transfract_rev(num):
   numlen = len(num)
   dec_num = 0
   for i in range(numlen):
      if int(num[i]) == 0:
         continue
      dec_num += float(num[i])* (3 ** (-(i+1)))
   return dec_num
   
# Кнопка перевода из десятичной в троичную
def btnequal(event):
    e = equa.get()
    if e == '' or e.count('.') > 1 or e.find('-') > 0 or e.count('-') > 1:
       messagebox.showwarning("Warning","Ошибка ввода")
       clear_all()
       return 0
    pp = e.find('.')
    intpart = e[:pp]
    fpart = e[pp:]
    if pp == 0:
       intpart = 0
    if pp<0:
       intpart = e
       total = transint(intpart)
       tot.set(total)
       return 0
    total = transint(intpart) +'.' + transfract(fpart)
    tot.set(total)

# Пункт меню с переводом из десятичной в троичную
def btnequal1():
    e = equa.get()
    if e == '' or e.count('.') > 1 or e.find('-') > 0 or e.count('-') > 1:
       messagebox.showwarning("Warning","Ошибка ввода")
       clear_all()
       return 0
    pp = e.find('.')
    intpart = e[:pp]
    fpart = e[pp:]
    if pp == 0:
       intpart = 0
    if pp<0:
       intpart = e
       total = transint(intpart)
       tot.set(total)
       return 0
    total = transint(intpart) +'.' + transfract(fpart)
    tot.set(total)

# Кнопка перевода из троичной в десятичную
def btnequalrev(event):
    e = equa.get()
    total = ''
    zapr = ' 3456789'
    for i in e:
       if zapr.find(i) > 0:
          clear_all()
          messagebox.showwarning("Warning","Число не является троичным")
          return 0
    if e == '' or e.count('.') > 1 or e.find('-') > 0 or e.count('-') > 1:
       messagebox.showwarning("Warning","Ошибка ввода")
       print('eee')
       clear_all()
       return 0
    pp = e.find('.')
    intpart = e[:pp]
    fpart = e[pp+1:]
    if pp == 0:
       intpart = 0
    if pp<0:
       intpart = e
       total = transint_rev(intpart)
       tot.set(total)
       return 0
    total = transint_rev(intpart) + transfract_rev(fpart)
    total = round(total,6)
    tot.set(total)

# Пункт меню с переводом из троичной в десятичную
def btnequalrev1():
    e = equa.get()
    total = ''
    zapr = ' 3456789'
    for i in e:
       if zapr.find(i) > 0:
          clear_all()
          messagebox.showwarning("Warning","Число не является троичным")
          return 0
    if e == '' or e.count('.') > 1 or e.find('-') > 0 or e.count('-') > 1:
       messagebox.showwarning("Warning","Ошибка ввода")
       print('eee')
       clear_all()
       return 0
    pp = e.find('.')
    intpart = e[:pp]
    fpart = e[pp+1:]
    if pp == 0:
       intpart = 0
    if pp<0:
       intpart = e
       total = transint_rev(intpart)
       tot.set(total)
       return 0
    total = transint_rev(intpart) + transfract_rev(fpart)
    total = round(total,6)
    tot.set(total)

# Функции нажатия на кнопки
def press0(event):
    e = equa.get()
    e = e + '0'
    equa.set(e)
    equation.set(e)
    
def press1(event):
    e = equa.get()
    e = e + '1'
    equa.set(e)
    equation.set(e)

def press2(event):
    e = equa.get()
    e = e + '2'
    equa.set(e)
    equation.set(e)

def press3(event):
    e = equa.get()
    e = e + '3'
    equa.set(e)
    equation.set(e)

def press4(event):
    e = equa.get()
    e = e + '4'
    equa.set(e)
    equation.set(e)

def press5(event):
    e = equa.get()
    e = e + '5'
    equa.set(e)
    equation.set(e)

def press6(event):
    e = equa.get()
    e = e + '6'
    equa.set(e)
    equation.set(e)

def press7(event):
    e = equa.get()
    e = e + '7'
    equa.set(e)
    equation.set(e)

def press8(event):
    e = equa.get()
    e = e + '8'
    equa.set(e)
    equation.set(e)

def press9(event):
    e = equa.get()
    e = e + '9'
    equa.set(e)
    equation.set(e)

def press_(event):
    e = equa.get()
    e = e + '-'
    equa.set(e)
    equation.set(e)

def pressp(event):
    e = equa.get()
    e = e + '.'
    equa.set(e)
    equation.set(e)

# Функция очистки всего
def clear_all():
    equa.set('')
    equation.set("_____________")
    tot.set("_____________")

# Функция очистки выражения
def clear_ans():
    equa.set('')
    equation.set("_____________")

# Функция с окном информации
def info():
   root = Tk()
   root.title("Info")
   root.resizable(width = False, height = False)
   root.wm_attributes("-topmost", 1)
   inform = '''    Калькулятор для перевода
 чисел из десятичной системы в
      троичную и обратно
                ИУ7 - 21Б
           Сангинов Азамат'''
   inf = Text(root, bg = 'red', font='Arial 10', width = 28, height = 5)
   inf. insert('0.0',inform)
   inf.grid(row = 2, columnspan = 8)
   root.mainloop()

   
### Main ###
root = Tk()
root.title("Калькулятор")
root.minsize(440 , 170)
root.resizable(width = True, height = True)

equa = StringVar()
equa.set('')
equation = StringVar()
calculation = Label(root, textvariable = equation)
equation.set("_____________")
calculation.grid(row=2, column = 4, columnspan=10)
tex = Label(root, text='Исходное число:').grid(row = 2, column = 1)
tex1 = Label(root, text='Переведенное число:').grid(row = 3, column = 1)
tot = StringVar()
output = Label(root, textvariable = tot)
tot.set("_____________")
output.grid(row=3, column = 4, columnspan=8)

butt0 = Button(root, text="0")
butt0.grid(row = 7, column = 3, padx=10, pady=10)
butt0.bind("<Button-1>",press0)
butt1 = Button(root, text="1")
butt1.grid(row = 4, column = 2, padx=5, pady=5)
butt1.bind("<Button-1>",press1)
butt2 = Button(root, text="2")
butt2.grid(row = 4, column = 3, padx=5, pady=5)
butt2.bind("<Button-1>",press2)
butt3 = Button(root, text="3")
butt3.grid(row = 4, column = 4, padx=5, pady=5)
butt3.bind("<Button-1>",press3)
butt4 = Button(root, text="4")
butt4.grid(row = 5, column = 2, padx=5, pady=5)
butt4.bind("<Button-1>",press4)
butt5 = Button(root, text="5")
butt5.grid(row = 5, column = 3, padx=5, pady=5)
butt5.bind("<Button-1>",press5)
butt6 = Button(root, text="6")
butt6.grid(row = 5, column = 4, padx=5, pady=5)
butt6.bind("<Button-1>",press6)
butt7 = Button(root, text="7")
butt7.grid(row = 6, column = 2, padx=5, pady=5)
butt7.bind("<Button-1>",press7)
butt8 = Button(root, text="8")
butt8.grid(row = 6, column = 3, padx=5, pady=5)
butt8.bind("<Button-1>",press8)
butt9 = Button(root, text="9")
butt9.grid(row = 6, column = 4, padx=5, pady=5)
butt9.bind("<Button-1>",press9)
buttmin = Button(root, text="-")
buttmin.grid(row = 7, column = 4, padx=5, pady=5)
buttmin.bind("<Button-1>",press_)
clear_alll = Button(root, text="AC", command = clear_all)
clear_alll.grid(row = 7, column = 2, padx=5, pady=5)
clear_anss = Button(root, text="C", command = clear_ans)
clear_anss.grid(row = 8, column = 2, padx=5, pady=5)
point = Button(root, text=".")
point.grid(row = 7, column = 5, padx=5, pady=5)
point.bind("<Button-1>",pressp)
equal1 = Button(root, text="10 --> 3")
equal1.grid(row=8, column=3, padx=5, pady=5)
equal1.bind("<Button-1>",btnequal)
equal2 = Button(root, text="3 --> 10")
equal2.grid(row=8, column=4, padx=5, pady=5)
equal2.bind("<Button-1>",btnequalrev)

menubar = Menu(root)

menubar.add_command(label = '10 --> 3', command = btnequal1)
menubar.add_command(label = '3 --> 10', command = btnequalrev1)

clear_menu = Menu(menubar, tearoff=0)
clear_menu.add_command(label="Очистить выражение", command = clear_ans)
clear_menu.add_command(label="Очистить все", command= clear_all)
menubar.add_cascade(label="Очистить", menu=clear_menu)

menubar.add_command(label = 'Инфо', command = info)

root.config(menu=menubar)
root.mainloop()
