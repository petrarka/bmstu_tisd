x = float(input('X = '))
eps = float(input('eps = '))
nmax = int(input('Nmax = '))

s = 1
t = 1
n = 0
st = -1

while abs(t) >= eps:
    n += 1
    t *= x * (-0.5)**n * ((2*n-1)/n)
    s += t
    if n == nmax:
        st = 1
        break

print()

if st>0:
    print('Ряд НЕ сошелся за',n,'итераций')
else:
    print('Ряд сошелся за',n,'итераций')

if s > 1000:
    print('Сумма ряда =','{:4.2e}'.format(s))
else:
    print('Сумма ряда =','{:4.2f}'.format(s))
