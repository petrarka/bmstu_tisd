an = input('Размер массива: ')
q=1
if len(an) == 0:
    print('Нужно было ввести размер!!')
    q = -1
for j in an:
    if ord(j) not in range(48,59):
        print('Разрешено вводить только целые числа!!')
        q=-1
        break
if q > 0:
    k = 1
    an = int(an)
    print('Заполните список')
    a = [input() for n in range(an)]
    b = []*len(a)
    x = len(a)
    if x == 0:
        print('Пустой список')
        k = -1
    if x == 1:
        print('Едиственный элемент: ',a[0])
        k = -1
    for i in a:
        if i.isalpha() or i == '.' or i == '':
            print('Ошибка, разрешено вводить только числа!\n')
            k = -1
            break
        i = float(i)
        b.append(i)

    if k>0:
        m1 = max(b)
        m2 = max(b)
        print('\nИсходный список: ',b,'\n')
        
        for j in range(len(b)):
            if b[j] <= m1:
                m1 = b[j]
                i1 = j
        for j in range(len(b)):
            if b[j] <= m2 and j != i1:
                m2 = b[j]
                i2 = j
        
        print('Минимальный элемент номер 1: ',m1)
        print('Минимальный элемент номер 2: ',m2,'\n')
        l = abs(i2-i1) - 1
        print('Расстояние между ними: ',l)







