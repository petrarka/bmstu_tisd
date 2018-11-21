from math import *
from tkinter import *
global x_v,y_v
y_v = []
x_v = []
def inserter(value,value1):
    output.insert('0.0 ',value1)
    output.insert('1.0 ',' ; ')
    output.insert('1.0 ',value)
    output.insert('1.0 ','\n')
    
def handler():
    dots = []
    x_val = float(x_.get())
    y_val = float(y_.get())
    x_v.append(x_val)
    y_v.append(y_val)
    inserter(x_val,y_val)

def solve():
    Firs_x = -500
    for i in range(1200):
        x = First_x + (1 / 16) * i
        y = -(i) + 500
        #x += 500
        canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
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
output = Text(frame, bg = 'lightblue', font='Arial 10', width = 35, height = 10)
butt = Button(frame, text='Solve',command = solve).grid(row = 1, column = 6, padx = (10,0))
output.grid(row = 2, columnspan = 8)
    
canv.pack() 
root.mainloop()
root1.mainloop()
