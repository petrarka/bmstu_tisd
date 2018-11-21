from math import sqrt
ax = float(input('Введите координату x первой точки: '))
ay = float(input('Введите координату y первой точки: '))
bx = float(input('Введите координату x второй точки: '))
by = float(input('Введите координату y второй точки: '))
cx = float(input('Введите координату x третьей точки: '))
cy = float(input('Введите координату y третьей точки: '))

ab = sqrt((ax-bx)**2 + (ay-by)**2)
bc = sqrt((bx-cx)**2 + (by-cy)**2)
ca = sqrt((cx-ax)**2 + (cy-ay)**2)

if(ab >= bc and ab >= ca):
    bis = sqrt(bc*ca * (bc+ca+ab) * (bc+ca-ab)) / (bc+ca)
elif(bc >= ab and bc >= ca):
    bis = sqrt(ab*ca * (ab+ca+bc) * (ab+ca-bc)) / (ab+ca)
else:
    bis = sqrt(bc*ab * (bc+ab+ca) * (bc+ab-ca)) / (bc+ab)
print('\nБиссектриса из наибольшего угла равна ','{:.4f}' .format(bis))
