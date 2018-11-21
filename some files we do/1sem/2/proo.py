from math import sin
def func(x):
    return x*x

def integr(a,b,n):
    s = 0
    h = (b-a)/(2*n)
    s2=s4=0
    if a<0 and b>0:
        return (integr(a,0,n)+integr(0,b,n))
    for i in range(0,2*n-1,2):
        s4+=func(a+h*i)
        s2+=func(a+h*(i+1))

    s = (h/3)*(func(a) + 4*s4 + 2*s2-func(b))
    return s

a = float(input('a '))
b = float(input('b '))
n = int(input('n '))
ina = round(integr(a,b,n),4)

print(ina)
