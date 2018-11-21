from math import *
n = int(input('Сколько точек: '))
x_v = []
y_v = []
if n < 3:
   print('Мало точек')
else:
   for i in range(n):
      x = float(input('X: '))
      y = float(input('Y: '))
      x_v.append(x)
      y_v.append(y)
   fl = True
   k = 0
   for i in range(n):
      if not fl:
         break
      ax = x_v[i]
      ay = y_v[i]
      for j in range(n-1,0,-2):
         bx = x_v[j]
         by = y_v[j]
         cx = x_v[j-1]
         cy = y_v[j-1]
         if(ax == bx and bx == cx and ay == by and by == cy):
            continue
         elif(ay == by and ay == cy and cy == ay):
            continue
         elif(ax == bx and ax == cx and cx == ax):
            continue
         elif(bx-ax)*(cy-ay) == (cx-ax)*(by-ay):
            continue
         else:
            k+=1
            ab = sqrt((ax-bx)**2 + (ay-by)**2)
            bc = sqrt((bx-cx)**2 + (by-cy)**2)
            ca = sqrt((cx-ax)**2 + (cy-ay)**2)
            polpir = (ab+bc+ca)/2
            sm = sqrt(polpir*(polpir-ab)*(polpir-bc)*(polpir-ca))
            if fl:
               maxs = sm
               A = ab
               B = bc
               C = ca
               x1 = ax
               y1 = ay
               x2 = bx
               y2 = by
               x3 = cx
               y3 = cy
               fl = False
            if sm>=maxs:
               maxs = sm
               A = ab
               B = bc
               C = ca
               x1 = ax
               y1 = ay
               x2 = bx
               y2 = by
               x3 = cx
               y3 = cy
   if k:
      print('AB;',A)
      print('BC;',B)
      print('CA;',C)
      print('S=',maxs)
      print(x1,x2,x3)
      print(y1,y2,y3)
   else:
      print('Нельзя построить треугольник')
            
