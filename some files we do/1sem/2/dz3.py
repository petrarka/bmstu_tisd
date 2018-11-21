# Программа для определения длинн сторон треугольника по заданным точкам вершин
# определения биссектрисы из большего угла, для проверки наличия точки внутри
# треугольника и определения расстояния от точки до ближайшей стороны
#                                                       Сангинов Азамат ИУ7-11Б


# ax,ay, bx,by, cx,cy - коордитаны вершин треугольника
# a, b, c - стороны треугольника
# bis - биссектриса треугольника
# ox, oy - координаты точки для проверки
# r1,r2, r3 - рабочие переменные
# oa, ob, oc - расстояние от точки O до вершин треугольника
# pa - полупериметр треугольника OAB
# pb - полупериметр треугольника OBC
# pc - полупериметр треугольника OBA
# ra, rb, rc - расстояние от точки O до прямых a, b, c

from math import sqrt

ax = float(input('Введите координату x первой точки: '))
ay = float(input('Введите координату y первой точки: '))
bx = float(input('Введите координату x второй точки: '))
by = float(input('Введите координату y второй точки: '))
cx = float(input('Введите координату x третьей точки: '))
cy = float(input('Введите координату y третьей точки: '))

ab = sqrt(abs(ax-bx)**2 + abs(ay-by)**2)
bc = sqrt(abs(bx-cx)**2 + abs(by-cy)**2)
ca = sqrt(abs(cx-ax)**2 + abs(cy-ay)**2)

if(ab > ca):
    ab,ca = ca,ab
   # ax,cx = cx, ax
   # ay,cy = cy, ay
   # print(ax,ay)
elif(bc > ca):
    bc,ca = ca,bc
   # bx,cx = cx, ax
   # by,cy = cy, by
   # print(bx,by)
ab = round(ab, 4)
bc = round(bc, 4)
ca = round(ca, 4)


# Проверка треугольника на существование
if(ax == bx and bx == cx and ay == by and by == cy):
    print('Треугольник не существует, все точки имеют одинаковые координаты')
elif(ay == by and ay == cy and cy == ay):
    print('Треугольник не существует,все точки образуют горизонтальную прямую')
elif(ax == bx and ax == cx and cx == ax):
    print('Треугольник не существует, все точки образуют вертикальную прямую')
elif(ab + bc <= ca or ab + ca <= bc or bc + ca <= ab):
    print('Все точки образуют диагональную прямую')
else:
    
    if(ab == bc or bc == ca or ab == ca):
        print('\nТреугольник равнобедренный')
    else:
        print('\nТреугольник не является равнобедренным')
        
    print('\nДлина стороны ab = ','{:.4f}' .format(ab))
    print('Длина стороны bc = ','{:.4f}' .format(bc))
    print('Длина стороны ca = ','{:.4f}' .format(ca))
    
    bis = sqrt(ab*bc * (ab+bc+ca) * (ab+bc-ca)) / (ab+bc)
    print('\nБиссектриса из большего угла равна ','{:.4f}' .format(bis))

    ox = float(input('\nВведите координату x точки O для проверки: '))
    oy = float(input('Введите координату y точки O для проверки: '))

   ''' oa = sqrt(abs(ax-ox)**2 + abs(ay-oy)**2)
    ob = sqrt(abs(bx-ox)**2 + abs(by-oy)**2)
    oc = sqrt(abs(cx-ox)**2 + abs(cy-oy)**2)

    ppabc = (ab + bc + ca)/2
    ppoab = (oa + ob +  ab)/2
    ppobc = (oc + ob +  bc)/2
    ppoac = (oa + oc +  ca)/2
    pabc = sqrt(abs(ppabc * (ppabc-ab) * (ppabc-bc) * (ppabc-ca)))
    poab = sqrt(abs(ppoab * (ppoab-oa) * (ppoab-ob) * (ppoab-ab)))
    pobc = sqrt(abs(ppobc * (ppobc-oc) * (ppobc-ob) * (ppobc-bc)))
    poac = sqrt(abs(ppoac * (ppoac-oa) * (ppoac-oc) * (ppoac-ca)))

    
    ra = (2 * ppoab) / ab
    rb = (2 * ppobc)/ bc
    rc = (2 * ppoac) / ca
    r1 = (ax-ox)*(by-ay) - (bx-ax)*(ay-oy)
    r2 = (bx-ox)*(cy-by) - (cx-bx)*(by-oy)
    r3 = (cx-ox)*(ay-cy) - (ax-cx)*(cy-oy)
    if(( r1 >= 0 and r2 >= 0 and r3 >=0) or (r1 <= 0 and r2 <= 0 and r3 <=0)):
        print('1')
        oa = sqrt(abs(ax-ox)**2 + abs(ay-oy)**2)
        ob = sqrt(abs(bx-ox)**2 + abs(by-oy)**2)
        oc = sqrt(abs(cx-ox)**2 + abs(cy-oy)**2)
        pa = (oa + ob + ab)/2
        pb = (ob + oc + bc)/2
        pc = (oc + oa + ca)/2
        ra = (2* sqrt(abs(pa * (pa-ab) * (pa-bc) * (pa-ca))))/ab
        rb = (2* sqrt(abs(pb * (pb-ab) * (pb-bc) * (pb-ca))))/bc
        rc = (2* sqrt(abs(pc * (pc-ab) * (pc-bc) * (pc-ca))))/ca
        if (ra == 0):
            print('\nТочка лежит на стороне a')
        elif(rb == 0):
            print('\nТочка лежит на стороне b')
        elif(rc == 0):
            print('\nТочка лежит на стороне c')
        elif(ra < rb and ra < rc):
            print('\nТочка внутри, расстояние до ab = ','{:.4f}' .format(ra))
        elif(rb < ra and rb < rc):
            print('\nТочка внутри, расстояние до bc = ','{:.4f}' .format(rb))
        elif(rc < ra and rc < rb):
            print('\nТочка внутри, расстояние до ca = ','{:.4f}' .format(rc))
        else:
            print('error')'''
    
# Проверка: находится ли точка O внутри треугольника
    r1 = (ax-ox)*(by-ay) - (bx-ax)*(ay-oy)
    r2 = (bx-ox)*(cy-by) - (cx-bx)*(by-oy)
    r3 = (cx-ox)*(ay-cy) - (ax-cx)*(cy-oy)
    if(( r1 >= 0 and r2 >= 0 and r3 >=0) or (r1 <= 0 and r2 <= 0 and r3 <=0)):
        oa = sqrt(abs(ax-ox)**2 + abs(ay-oy)**2)
        ob = sqrt(abs(bx-ox)**2 + abs(by-oy)**2)
        oc = sqrt(abs(cx-ox)**2 + abs(cy-oy)**2)
        pa = (oa + ob + ab)/2
        pb = (ob + oc + bc)/2
        pc = (oc + oa + ca)/2
        ra = (2* sqrt(abs(pa * (pa-ab) * (pa-bc) * (pa-ca))))/ab
        rb = (2* sqrt(abs(pb * (pb-ab) * (pb-bc) * (pb-ca))))/bc
        rc = (2* sqrt(abs(pc * (pc-ab) * (pc-bc) * (pc-ca))))/ca
        
        if (ra == 0):
            print('\nТочка лежит на стороне a')
        elif(rb == 0):
            print('\nТочка лежит на стороне b')
        elif(rc == 0):
            print('\nТочка лежит на стороне c')
        elif(ra < rb and ra < rc):
            print('\nТочка внутри, расстояние до a = ','{:.4f}' .format(ra))
        elif(rb < ra and rb < rc):
            print('\nТочка внутри, расстояние до b = ','{:.4f}' .format(rb))
        elif(rc < ra and rc < rb):
            print('\nТочка внутри, расстояние до c = ','{:.4f}' .format(rc))
    else:
       print('\nТочка не находится внутри треугольника')
