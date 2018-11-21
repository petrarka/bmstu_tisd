from tkinter import *
from random import *
import time
from decimal import *

def sw(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
    
def ch_sort(arr):
    t1 = Decimal(time.time())
    i = len(arr)
    while i > 1:
        m = 0
        for j in range(i):
            if arr[j] > arr[m]:
                m = j
        sw(arr,i-1,m)
        i-=1
    t2 = Decimal(time.time())
    t2 = t2 - t1
    return arr, t2
    
    

def st():
    n = int(n1.get())
    arr = [randint(-100,100) for i in range(n)]
    arr_text = ''
    for i in range(n):
        arr_text += str(arr[i]) + ' '
    arr_lab = Label(root,text = arr_text)
    arr_lab.grid(row = 4,column = 2)
    arr1,stime = ch_sort(arr)
    arr1_text = ''
    for i in range(n):
        arr1_text += str(arr1[i]) + ' '
    arr1_lab = Label(root,text = arr1_text)
    arr1_lab.grid(row = 5, column = 2)
    t_lab = Label(root,text = str(stime))
    t_lab.grid(row = 6, column = 2)
    h2_lab.grid(row = 6,column = 1)
    
root = Tk()
root.title("Сортировка выбором")
root.minsize(300 , 170)
root.resizable(width = True, height = True)

t1 = Label(root, text = 'N', width = 10)
t1.grid(row = 1, column = 1)
n1 = Entry(root, width = 5)
n1.grid(row = 2, column = 1)

h_lab = Label(root,text = 'Исходный: ')
h_lab.grid(row = 4,column = 1)
h1_lab = Label(root,text = 'Отсортированный: ')
h1_lab.grid(row = 5,column = 1)
h2_lab = Label(root, text = 'Время')

start_butt = Button(root, text = 'Start',command = st)
start_butt.grid(row = 3, column = 1)

root.mainloop()
