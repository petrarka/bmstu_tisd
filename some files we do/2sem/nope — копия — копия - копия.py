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
def btnequal():
    e = calculation.get()
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
def btnequalrev():
    e = calculation.get()
    total = ''
    zapr = ' 3456789'
    for i in e:
       if zapr.find(i) > 0:
          clear_all()
          messagebox.showwarning("Warning","Число не является троичным")
          return 0
    if e == '' or e.count('.') > 1 or e.find('-') > 0 or e.count('-') > 1:
       messagebox.showwarning("Warning","Ошибка ввода")
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
def press0(num):
    l = len(calculation.get())
    calculation.insert(l,num)

# Функция очистки всего
def clear_all():
   l = len(calculation.get())
   calculation.delete(0,l)
   tot.set('')

# Функция очистки выражения
def clear_ans():
    tot.set('')

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

calculation = Entry(root, width = 20)
calculation.grid(row=2, column = 4, columnspan=10)
tex = Label(root, text='Исходное число:').grid(row = 2, column = 1)
tex1 = Label(root, text='Переведенное число:').grid(row = 3, column = 1)
tot = StringVar()
output = Label(root, textvariable = tot)
output.grid(row=3, column = 4, columnspan=8)

butt0 = Button(root, text="0", command = lambda: press0('0'))
butt0.grid(row = 7, column = 3, padx=10, pady=10)
butt1 = Button(root, text="1", command = lambda: press0('1'))
butt1.grid(row = 4, column = 3, padx=10, pady=10)
butt2 = Button(root, text="2", command = lambda: press0('2'))
butt2.grid(row = 4, column = 4, padx=10, pady=10)
butt3 = Button(root, text="3", command = lambda: press0('3'))
butt3.grid(row = 4, column = 5, padx=10, pady=10)
butt4 = Button(root, text="4", command = lambda: press0('4'))
butt4.grid(row = 5, column = 3, padx=10, pady=10)
butt5 = Button(root, text="5", command = lambda: press0('5'))
butt5.grid(row = 5, column = 4, padx=10, pady=10)
butt6 = Button(root, text="6", command = lambda: press0('6'))
butt6.grid(row = 5, column = 5, padx=10, pady=10)
butt7 = Button(root, text="7", command = lambda: press0('7'))
butt7.grid(row = 6, column = 3, padx=10, pady=10)
butt8 = Button(root, text="8", command = lambda: press0('8'))
butt8.grid(row = 6, column = 4, padx=10, pady=10)
butt9 = Button(root, text="9", command = lambda: press0('9'))
butt9.grid(row = 6, column = 5, padx=10, pady=10)
buttmin = Button(root, text = '-', command = lambda: press0('-'))
buttmin.grid(row = 7, column = 4, padx=5, pady=5)
point = Button(root, text = '.', command = lambda: press0('.'))
point.grid(row = 7, column = 5, padx=5, pady=5)
clear_alll = Button(root, text = 'AC', command = clear_all)
clear_alll.grid(row = 4, column = 2, padx=5, pady=5)
clear_anss = Button(root,text = 'C',command = clear_ans)
clear_anss.grid(row = 5, column = 2, padx=5, pady=5)
equal1 = Button(root, text = '10 --> 3', command = btnequal)
equal1.grid(row=6, column=2, padx=5, pady=5)
equal2 = Button(root, text = '3 --> 10', command = btnequalrev)
equal2.grid(row=7, column=2, padx=5, pady=5)

menubar = Menu(root)

menubar.add_command(label = '10 --> 3', command = btnequal)
menubar.add_command(label = '3 --> 10', command = btnequalrev)

clear_menu = Menu(menubar, tearoff=0)
clear_menu.add_command(label="Очистить выражение", command = clear_ans)
clear_menu.add_command(label="Очистить все", command= clear_all)
menubar.add_cascade(label="Очистить", menu=clear_menu)

menubar.add_command(label = 'Инфо', command = info)

root.config(menu=menubar)
root.mainloop()
