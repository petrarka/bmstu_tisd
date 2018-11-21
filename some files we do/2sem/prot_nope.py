from tkinter import *
from math import *
def solve():
    l = len(s1pole.get())
    s1pole.delete(0,l)
    a = float(polea.get())
    b = float(poleb.get())
    c = float(polec.get())
    
    if(a != 0):
        d = b*b - 4*a*c
        if (d == 0):
            x = -b/2*a
            s = 'Корень кратности 2: x = ' + str(x)
            s1pole.insert('0',s)
        elif (d > 0):
            x = (-b + sqrt(d))/(2*a)
            s1 = 'x1 = ' + str(x) + '; '
            x = (-b - sqrt(d))/(2*a)
            s = s1 + 'x2 = ' + str(x)
            s1pole.insert('0',s)
        elif (d < 0):
            s1pole.insert('0','Нет действительных решений')
    elif( a == 0 and b != 0):
        x = -c/b
        s = 'Линейное уравнение: x = ' + str(x)
        s1pole.insert('0',s)
    elif( a == 0 and b == 0 and c == 0):
        s1pole.insert('0','x - любое число')
    elif( a == 0 and b == 0 and c != 0):
        s1pole.insert('0','Нет решений')
        

root = Tk()
root.title('Квадратное уравнение')
root.resizable(width = True, height = True)

apole = Label(root,text = 'a', width = 5, height = 1)
apole.grid(row = 1, column = 1)
polea = Entry(root,width = 5)
polea.grid(row = 1, column = 2)
bpole = Label(root,text = 'b', width = 5, height = 1)
bpole.grid(row = 2, column = 1)
poleb = Entry(root,width = 5)
poleb.grid(row = 2, column = 2)
cpole = Label(root,text = 'c', width = 5, height = 1)
cpole.grid(row = 3, column = 1)
polec = Entry(root,width = 5)
polec.grid(row = 3, column = 2)

solve = Button(root,width = 5, text = 'Решить',command = solve)
solve.grid(row = 4, column = 1)

spole = Label(root,text = 'Ответ:', width = 5, height = 1)
spole.grid(row = 5, column = 1)
s1pole = Entry(root, width = 30)
s1pole.grid(row = 5, column = 2)

root.mainloop()



