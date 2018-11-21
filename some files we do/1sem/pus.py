from math import *
from tkinter import *
import os
global x_v,y_v
y_v = []
x_v = []
def checko(num):
    abc = (' 0123456789')
    k = 0 
    for i in range(len(num)):
        if abc.find(num[i]) > 0 or (num[i]=='-' or num[i] == '.' and abc.find(num[i+1]) > 0):
            k+=1
    print(k)
    if k == len(num):
        return num

def create_canv():
    canv.create_line(500, 1000, 500, 0, width = 2, arrow = LAST) 
    canv.create_line(0, 500, 1000, 500, width = 2, arrow = LAST) 
    for i in range(16000):
        if i % 800 == 0:
                k = First_x + (1 / 16) * i
                canv.create_line(k + 501, -2.5 + 500, k + 501, 2.5 + 500, width = 0.5, fill = 'black')
                canv.create_text(k + 500, -10 + 500, text = str(int(k) / 50), fill = 'blue', font = ('Arial', '10'))
        if k != 0:
                canv.create_line(-3 + 500, k + 501, 3 + 500, k + 501, width = 0.5, fill = 'black')
                canv.create_text(15 + 500, k + 500, text = str(-(int(k) / 50)), fill = 'blue', font = ('Arial', '10'))
            
def inserter(value,value1):
    output.insert('0.0 ',value1)
    output.insert('1.0 ',' ; ')
    output.insert('1.0 ',value)
    output.insert('1.0 ','\n')
    
def handler():
    output.delete('0.0 ','end')
    x_val = (x_.get())
    x = checko(x_val)
    y_val = (y_.get())
    y = checko(y_val)
    if x_val=='' or y_val == '':
        output.delete('0.0 ','end')
        output.insert('0.0 ','Неверные значения.\nКонец работы программы')
        sys.exit()
    if x == x_val and y == y_val:
        x_val = float(x_val)
        y_val = float(y_val)
        x_v.append(x_val)
        y_v.append(y_val)
        inserter(x_val,y_val)
    else:
        output.delete('0.0 ','end')
        output.insert('0.0 ','Неверные значения.')#\nКонец работы программы')
        sys.exit()

def solve():
   canv.delete("all")
   create_canv()
   firstx = 497
   firtsy = 497
   for i in range(len(x_v)):
      x = x_v[i]*50+firstx
      y = -y_v[i]*50+firtsy
      canv.create_oval(x, y, x + 5, y + 5, fill = 'black')
   triangle()
   
def triangle():
    fl = True
    firstx = 500
    firsty = 500
    rx1=rx2=rx3=ry1=ry2=ry3=0
    for i in range(len(x_v)):
        ax = x_v[i]
        ay = y_v[i]
        for j in range(len(x_v)-1,0,-2):
            bx = x_v[j]
            by = y_v[j]
            cx = x_v[j-1]
            cy = y_v[j-1]
            print(ax,ay)
            print(bx,by)
            print(cx,cy)
            if(ax == bx and bx == cx and ay == by and by == cy):
                continue
            elif(ay == by and ay == cy and cy == ay):
                continue
            elif(ax == bx and ax == cx and cx == ax):
                continue
            elif(bx-ax)*(cy-ay) == (cx-ax)*(by-ay):
                continue
            else:
                ab = sqrt((ax-bx)**2 + (ay-by)**2)
                bc = sqrt((bx-cx)**2 + (by-cy)**2)
                ca = sqrt((cx-ax)**2 + (cy-ay)**2)
                bis1 = sqrt(bc*ca * (bc+ca+ab) * (bc+ca-ab))/(bc + ca)
                bis2 = sqrt(ab*ca * (ab + ca + bc) * (ab + ca - bc))/(ab + ca)
                bis3 = sqrt(bc*ab * (bc + ab + ca) * (bc + ab - ca))/(bc + ab)
                bs = bis1 + bis2 + bis3
                if fl:
                    bissum = bs
                    rx1=ax*50+firstx
                    rx2=bx*50+firstx
                    rx3=cx*50+firstx
                    ry1=-ay*50+firsty
                    ry2=-by*50+firsty
                    ry3=-cy*50+firsty
                    fl = False
                if bs <= bissum:
                    bissum = bs
                    rx1=ax*50+firstx
                    rx2=bx*50+firstx
                    rx3=cx*50+firstx
                    ry1=-ay*50+firsty
                    ry2=-by*50+firsty
                    ry3=-cy*50+firsty
    if not fl:
        bissum = round(bissum,4)
        output.delete('0.0 ','end')
        output.insert('0.0 ','Минимальная сумма длин биссектрис\n')
        output.insert('2.0 ',bissum)
        canv.create_line(rx1, ry1, rx2, ry2, width = 4)
        canv.create_line(rx2, ry2, rx3, ry3, width = 4)
        canv.create_line(rx3, ry3, rx1, ry1, width = 4)
    else:
        output.delete('0.0 ','end')
        output.insert('0.0 ','Треугольник не удается построить.\nКонец работы программы')
        sys.exit()
    
root = Tk()
canv = Canvas(root, width = 1000, height = 1000, bg = 'white')
canv.create_line(500, 1000, 500, 0, width = 2, arrow = LAST) 
canv.create_line(0, 500, 1000, 500, width = 2, arrow = LAST) 

First_x = -500;

for i in range(16000):
    if i % 800 == 0:
            k = First_x + (1 / 16) * i
            canv.create_line(k + 501, -2.5 + 500, k + 501, 2.5 + 500, width = 0.5, fill = 'black')
            canv.create_text(k + 500, -10 + 500, text = str(int(k) / 50), fill = 'blue', font = ('Arial', '10'))
    if k != 0:
            canv.create_line(-3 + 500, k + 501, 3 + 500, k + 501, width = 0.5, fill = 'black')
            canv.create_text(15 + 500, k + 500, text = str(-(int(k) / 50)), fill = 'blue', font = ('Arial', '10'))

root1 = Tk()
root1.title('Ввод координат')
root1.minsize(240 , 170)
root1.resizable(width = True, height = True)
frame = Frame(root1)
frame.grid()

x_text = Label(frame, text='  x:').grid(row = 1, column = 1)
x_ = Entry(frame, width = 10)
x_.grid(row = 1, column = 2, padx = (10,0))
y_text = Label(frame, text='  y:').grid(row = 1, column = 3)
y_ = Entry(frame, width = 10)
y_.grid(row = 1, column = 4, padx = (10,0))

but = Button(frame, text='Ввести', command = handler).grid(row = 1, column = 5,padx=(10,0))
output = Text(frame, bg = 'red', font='Arial 10', width = 35, height = 10)
butt = Button(frame, text='Решить',command = solve).grid(row = 1, column = 6, padx = (10,0))
output.grid(row = 2, columnspan = 8)

canv.pack() 
root.mainloop()
root1.mainloop()
