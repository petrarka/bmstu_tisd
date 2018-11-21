## Сортировка вставками с бинарным поиском
##                  Сангинов Азамат ИУ7-21

## testtime, testarr - тестовый массив и время его сортировки
## n1, n2, n3 - поля для ввода размеров
## start_butt - кнопка запуска

from tkinter import *
from random import *
import time
from decimal import *

## Бинарный поиск индекса для вставки
## start - левый край
## end - правый край
## mid - середина отсортированной части
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

## Сортировка массива
## j - индекс для вставки
## val - элемент, проверяемый для вставки
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

##def insertion_sort(alist):
##   for index in range(1,len(alist)):
##
##     currentvalue = alist[index]
##     position = index
##
##     while position>0 and alist[position-1]>currentvalue:
##         alist[position]=alist[position-1]
##         position = position-1
##
##     alist[position]=currentvalue
##   return alist

## Измерение времени сортировок
## l - размер массива
def sort_time(l):
   t1, a, b,a = randarr(l)

   t21 = Decimal(time.time())
   a = insertion_sort(a)
   t22 = Decimal(time.time())
   
   a = list(reversed(a))
   t31 = Decimal(time.time())
   a = insertion_sort(a)
   t32 = Decimal(time.time())
   
   t2 = t22 - t21
   t3 = t32 - t31
   t1 = '{:4.3e}'.format(t1)
   t2 = '{:4.3e}'.format(t2)
   t3 = '{:4.3e}'.format(t3)
   return t1,t2, t3

## Генерация массива из случайных чисел
## n - размерность массива
## t1,t2 - время сортировки
def randarr(n):
   a = []
   s = ''
   ar = ''
   r = -100
   l = 100
   for i in range(n):
      a.append(randint(r,l))
      s += str(a[i])
      s += ' '
   t1 = Decimal(time.time())
   a = insertion_sort(a)
   t2 = Decimal(time.time())
   t2 = t2 - t1
   for i in range(n):
      ar += str(a[i])
      ar += ' '
   return t2,ar, s, a

## Проверка ввода
## num - введенное значение
def enter_check(num):
    abc = ('0123456789')
    for i in num:
        if abc.find(i) < 0:
            return False
        else:
            return True


## Создание таблицы со значениями
## arr1_len, arr2_len, arr3_len - размерности массивов
## t11, t12, t13..., t33 - время, за которое были отсортированы массивы
## table11,....table34 - ячейки таблицы
def start():
   arr1_len = n1.get()
   arr2_len = n2.get()
   arr3_len = n3.get()
   if enter_check(arr1_len) and enter_check(arr2_len) and enter_check(arr3_len):
       t12,t11,t13 = sort_time(int(arr1_len))
       t22,t21,t23 = sort_time(int(arr2_len))
       t32,t31,t33 = sort_time(int(arr3_len))
       time1 = Label(root, text = '->',width = 5)
       time1.grid(row = 8, column = 3)
       time2 = Label(root, text = 'rand',width = 5)
       time2.grid(row = 9, column = 3)
       time3 = Label(root, text = '<-',width = 5)
       time3.grid(row = 10, column = 3)
       table11 = Label(root,text = 'N = '+ arr1_len,width = 10, bg = 'white')
       table11.place(x = 320, y = 85)
       table21 = Label(root,text = 'N = '+ arr2_len,width = 10, bg = 'white')
       table21.place(x = 420, y = 85)
       table31 = Label(root,text = 'N = '+ arr3_len,width = 10, bg = 'white')
       table31.place(x = 520, y = 85)
       table12 = Label(root,text = t11,width = 10, bg = 'white')
       table12.place(x = 320, y = 110)
       table22 = Label(root,text = t21,width = 10, bg = 'white')
       table22.place(x = 420, y = 110)
       table32 = Label(root,text = t31,width = 10, bg = 'white')
       table32.place(x = 520, y = 110)
       table13 = Label(root,text = t12,width = 10, bg = 'yellow')
       table13.place(x = 320, y = 130)
       table23 = Label(root,text = t22,width = 10, bg = 'yellow')
       table23.place(x = 420, y = 130)
       table33 = Label(root,text = t32,width = 10, bg = 'yellow')
       table33.place(x = 520, y = 130)
       table14 = Label(root,text = t13,width = 10, bg = 'white')
       table14.place(x = 320, y = 150)
       table24 = Label(root,text = t23,width = 10, bg = 'white')
       table24.place(x = 420, y = 150)
       table34 = Label(root,text = t33,width = 10, bg = 'white')
       table34.place(x = 520, y = 150)
   else:
      messagebox.showwarning("Warning","Ошибка ввода")

root = Tk()
root.title("Сортировка бинарными вставками")
root.minsize(640 , 170)
root.resizable(width = True, height = True)


t1 = Label(root, text = 'N1', width = 10)
t1.grid(row = 1, column = 1)
t2 = Label(root, text = 'N2', width = 10)
t2.grid(row = 1, column = 2)
t3 = Label(root, text = 'N3', width = 10)
t3.grid(row = 1, column = 3)
n1 = Entry(root, width = 10)
n1.grid(row= 2, column = 1)
n2 = Entry(root, width = 10)
n2.grid(row= 2, column = 2)
n3 = Entry(root, width = 10)
n3.grid(row= 2, column = 3)

testtime, testarr,testtext,a = randarr(9)
t4 = Label(root, text = testtext)
t4.grid(row = 3, column = 2)
t5 = Label(root, text = 'Test array: ')
t5.grid(row = 3, column = 1)
t6 = Label(root, text = testarr)
t6.grid(row = 4, column = 2)
t7 = Label(root, text = 'Sorted array: ')
t7.grid(row = 4, column = 1)
t8 = Label(root, text = 'Time: ')
t8.grid(row = 5, column = 1)
t9 = Label(root, text = testtime)
t9.grid(row = 5, column = 2)

start_butt = Button(root, text = 'Start', command = start)
start_butt.grid(row = 5, column = 3)
root.mainloop()
