an = input('Размер квадратной матрицы: ')
q = 1
if len(an) == 0:
    q = -1
    print('Нужно было ввести размер!!')
for j in an:
    if ord(j) not in range(49,59) or len(an) == 0:
        q = -1
        print('Разрешено вводить только целые положительные цисла!')
        break
if q > 0:
    an = int(an)
    v = [0]*an
    l = 1
    print('Заполните матрицу')
    a = [[0]*an for i in range(an)]
    for i in range(an):
        if l > 0:
            for j in range(an):
                if l > 0:
                    a[i][j] = input()
                    if len(a[i][j]) == 0:
                           l = -1
                           break
                    f = a[i][j]
                    for k in range(len(f)):
                        if ord(f[k]) in range(48,59):
                            continue
                        elif f[k] == '.' and ord(f[k+1]) in range(48,59) and ord(f[k-1]) in range(48,59):
                            continue
                        elif f[k] == '-' and ord(f[k+1]) in range(48,59):
                            continue
                        else:
                            l = -1
                            break
    if l < 0:
        print('Разрешено вводить только числа!!')
    else:
        for i in range(an):
            for j in range(an):
                a[i][j] = float(a[i][j])
                if a[i][j] >= 0:
                    v[j]+=1
        print('Исходная матрица')
        for q in a:
            print(q)
        mv = max(v)
        mv = v.index(mv)
        
        if max(v) == 0:
          print('Все элементы отрицательные')
        else:
            print('\nСтолбец с наименьшим количеством отрицательных элементов ',mv+1)
        xc = []
        print()
        for i in range(an-1):
            for j in range(1,an-i):
                xc.append(a[i][i+j])
        print('Массив с элементами над побочной диагональю: ',xc)
