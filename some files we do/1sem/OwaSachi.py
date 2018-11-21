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
        an = int(an)
        print('Заполните список')
        a = [input() for n in range(an)]
        b = []*len(a)
        k=1
        x = len(a)
        
        if x == 0:
            print('Пустой список')
            k = -1
            
        for i in a:
            if i.isalpha() or i == '.' or i == '':
                print('Ошибка, нужно заполнить список числами!')
                k = -1
                break
            i = float(i)
            b.append(i)
            
        e = 0
        if k>0:
            for j in b:
                if j > 0:
                    pp = j
                    e = -1
                    break
            if e < 0:
                print('Исходный список: ',a)
                ppi = b.index(pp)
                r = b[:ppi+1]
                if ppi == 0:
                    r =  b[ppi::2]
                elif ppi%52 == 0:
                    r += b[ppi+2::2]
                else:
                    r += b[ppi+1::2]
                print("Измененный список: ",r)
            else:
                print('Нет положительных элементов')
