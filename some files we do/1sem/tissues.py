import pickle
import os
import os.path
############### Открытие ###############
def open_db(name):
        with open(name, 'rb') as f:
            return pickle.load(f)

############### Поиск ###############
def _qual(**kwargs):
    return lambda row: all(row.get(k) == v for k, v in kwargs.items())

############### Добавление ############### 
def save_db(name, data):
    with open(name, 'wb') as f:
            pickle.dump(data, f)

############### Поиск ###############
def search(items, filter):
    return [item for item in items if filter(item)]

############### Показать все элементы ###############
def show(items):
    if items == []:
        print('База данных пуста')
    else:
            for i in items:
                if i == {}:
                        continue
                else:
                        s = i.get('Name')
                        print('Имя: ', '{:16s}'.format(s),'|',end='')
                        s = i.get('Class')
                        print('Класс: ', '{:5s}'.format(s),'|',end='')
                        s = i.get('Laid_down')
                        print('Спущен на воду: ', '{:7d}'.format(s),'|',end='')
                        s = i.get('Struck')
                        print('Утилизирован: ', '{:7d}'.format(s))

############### Удаление элемента ###############     
def deleto(items):
    abc = (' 1234')
    k = 0
    f = True
    while f:
        inpt = input('''Фильтр для удаления
1.Имя
2.Класс
3.Спущен на воду
4.Ушел в утиль\n''')
        if abc.find(inpt)>0:
            f = False
        
    if inpt == '1':
        filt = 'Name'
        value = input('Имя ')
    elif inpt == '2':
        filt = 'Class'
        value = input('Класс ')
    elif inpt == '3':
        filt = 'Laid_down'
        value = input('Год спуска на воду ')
        while not checko(value):
            value = input('Год спуска на воду: ')
        value = int(value)
    elif inpt == '4':
        filt = 'Struck'
        value = input('Год утилизации ')
        while not checko(value):
            value = input('Год утилизации: ')
        value = int(value)
    for i in range(len(items)):
            prom = items[i].get(filt)
            if prom == value:
                    items[i].clear()
                    k+=1
    if k:
            show(items)
    else:
        print('Не найдено')

############### Проверка ###############
def checko(year):
    abc = (' 0123456789')
    for i in year:
        if abc.find(i)<=0:
            return False
    return True

############### Поиск элемента ###############
def choice_search():
    se = []
    abc = (' 123456')
    f = True
    while f:
        inpt = input('''Фильтр для поиска
1.Имя
2.Класс
3.Спущен на воду
4.Год утилизации
5.Имя и класс
6.Год спуска на воду и год утилизации \n''')
        if abc.find(inpt)>0:
            f = False
    if inpt == '1':
        value = input('Имя: ')
        se = search(items,_qual(Name=value))
    elif inpt == '2':
        value = input('Класс: ')
        se = search(items,_qual(Class=value))
    elif inpt == '3':
        value = input('Год спуска на воду: ')
        while not checko(value):
            value = input('Год спуска на воду: ')
        value = int(value)
        se = search(items,_qual(Laid_down=value))
    elif inpt == '4':
        value = input('Год утилизации: ')
        while not checko(value):
            value = input('Год утилизации: ')
        value = int(value)
        se = search(items,_qual(Struck=value))
    elif inpt == '5':
        value = input('Имя: ')
        value1 = input('Класс: ')
        se = search(items,_qual(Name=value,Class=value1))
    elif inpt == '6':
        value = input('Год спуска на воду: ')
        value1 = input('Год утилизации: ')
        while not checko(value) and not checko(value1):
            value = input('Год спуска на воду: ')
            value1 = input('Год утилизации: ')
        value = int(value)
        value1 = int(value1)
        se = search(items,_qual(Laid_down=value,Struck=value1))
    if se == []:
        return print('Не найдено!')
    show(se)
    return se,value

############### Проверка названия ###############
def fncheck(ndb):
    abc = (' ~"#%&*:<>?/\{|}.')
    for i in ndb:
        if abc.find(i) > 0 or ndb.isspace():
            return True
    return False

############### Добавление элемента ###############
def appen(items):
    name = input('Имя: ')
    name = name[0].upper() + name[1:]
    flo = True
    while flo:
        laid_down = input('Год спуска на воду: ')
        while not checko(laid_down):
                laid_down = input('Год спуска на воду: ')
        struck = input('Год утилизации: ')
        while not checko(struck):
                struck = input('Год утилизации: ')
        laid_down = int(laid_down)
        struck = int(struck)
        if laid_down <= struck:
           flo = False
    classo = input('Класс: ')
    classo = classo.upper()
    items.append(dict(Name = name, Laid_down = laid_down, Struck = struck, Class = classo))

############### Главное меню ###############
def vibor():
    nu = (' 1234567')
    f = 1
    while f == 1:
        i = input('''\n1. Создать БД
2. Открыть БД
3. Просмотр всех элементов БД
4. Добавление новой записи в открытую БД
5. Поиск элементов в БД
6. Удаление элементов из БД
7. Выход
Выберите опцию: ''')
        if nu.find(i)>0:
            f = 3
    return(i)


save_db('test.bin', [
	dict(Name = 'Shimakaze', Laid_down = 1941, Struck = 1945, Class = 'DD'),
	dict(Name = 'Kirishima', Laid_down = 1912, Struck = 1942, Class = 'BB'),
	dict(Name = 'Yamato', Laid_down = 1937, Struck = 1945, Class = 'BB'),
	dict(Name = 'Hamakaze', Laid_down = 1939, Struck = 1945, Class = 'DD'),
	dict(Name = 'Kongou', Laid_down = 1911, Struck = 1945, Class = 'BB'),
        dict(Name = 'Akitsumaru', Laid_down = 1941, Struck = 1944, Class = 'LHA'),
        dict(Name = 'Bismarck', Laid_down = 1936, Struck = 1941, Class = 'BB'),
        dict(Name = 'Leberecht Maass', Laid_down = 1934, Struck = 1940, Class = 'DD'),
        dict(Name = 'Max Schultz', Laid_down = 1935, Struck = 1940, Class = 'DD'),
        dict(Name = 'Graf Zeppelin', Laid_down = 1936, Struck = 1947, Class = 'CV'),
        dict(Name = 'Saratoga', Laid_down = 1920, Struck = 1946, Class = 'CV'),
        dict(Name = 'Iowa', Laid_down = 1940, Struck = 2006, Class = 'BB'),
        dict(Name = 'Littorio', Laid_down = 1934, Struck = 1948, Class = 'BB'),
        dict(Name = 'Richelieu', Laid_down = 1935, Struck = 1968, Class = 'BB'),
        dict(Name = 'Gangut', Laid_down = 1909, Struck = 1956, Class = 'BB'),
])
ndb = 'test.bin'
openen = False
fl = True
while fl:
    i = vibor()
    print()       
    if i == '1':
        print()
        fname = True
        while fname: 
            ndb = input('Название БД ')
            fname = fncheck(ndb)
            if ndb == '':
                        fname = True
        ndb += '.bin'
        save_db(ndb,[])
        
    elif i == '2':
        print()
        osd = os.listdir()
        print('Список доступных БД:')
        for i in osd:
            if i[-4:] == '.bin':
                print(i[:-4])
        print()
        name = input('Название БД ')
        name += '.bin'
        if not os.path.isfile(name) or name[:-4].isspace() or name[:-4]==[]:
            print('Не найдено')
        else:
            items = open_db(name)
            show(items)
            openen = True

    elif i == '3':
        if openen:
            print()
            show(items)
            save_db(ndb,items)
            print()
        else:
            print('Нужно сначала открыть БД')
        
    elif i == '4':
        if openen:
            print()
            appen(items)
            save_db(ndb,items)
            print()
        else:
            print('Нужно сначала открыть БД')
        
    elif i == '5':
        if openen:
            print()
            choice_search()
            save_db(ndb,items)
            print()
        else:
            print('Нужно сначала открыть БД')
        
    elif i == '6':
        if openen:
            print()
            deleto(items)
            save_db(ndb,items)
        else:
            print('Нужно сначала открыть БД')

    elif i == '7':
        fl = False
