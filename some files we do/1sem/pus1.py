def in_function(x):
    return x

def calc_integra38(a,b,n):
    if a<0 and b>0:
        res = calc_integra38(a,0,n) + calc_integra38(0,b,n)
        return res
    res = in_function(a)+in_function(b)
    m = n*3
    h = (b-a)/(n*3)
    for i in range(1,m):
        x = a + h*i
        if i%3==0:
            res+=2*in_function(x)
        else:
            res+=3*in_function(x)
    res = (3/8) * res * h
    return res

a = float(input('a '))
b = float(input('b '))
n = int(input('n '))

if n%3==0:
    result = calc_integra38(a,b,n)
    print(result)
else:
    print('n%3 == 0')
