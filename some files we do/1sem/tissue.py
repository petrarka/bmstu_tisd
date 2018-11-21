import pickle

def open_db(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

def _qual(**kwargs):
    return lambda row: all(row.get(k) == v for k, v in kwargs.items())
    
def save_db(name, data):
    with open(name, 'wb') as f:
            pickle.dump(data, f)

def search(items, filter):
    return [item for item in items if filter(item)]

def choice_show():
    se = []
    inpt = int(input('''Что искать?
1.Имя
2.Класс
3.Спущен на воду
4.Поражение\n'''))
    value = input('Value: ')
    if inpt == 1:
        se = search(items,_qual(Name=value))
    elif inpt == 2:
        se = search(items,_qual(Class=value))
    elif inpt == 3:
        se = search(items,_qual(Laid_down=value))
    elif inpt == 4:
        se = search(items,_qual(Struck=value))
    if se == []:
        return print('Не найдено!')
    
    for i in se:
        s = i.get('Name')
        print('Name: ', '{:16s}'.format(s),'|',end='')
        s = i.get('Class')
        print('Class: ', '{:5s}'.format(s),'|',end='')
        s = i.get('Laid_down')
        print('Laid down: ', '{:7s}'.format(s),'|',end='')
        s = i.get('Struck')
        print('Struck: ', '{:7s}'.format(s))
    return se,value

save_db('test.db', [
	dict(Name = 'Shimakaze', Laid_down = '1941', Struck = '1945', Class = 'DD'),
	dict(Name = 'Kirishima', Laid_down = '1912', Struck = '1942', Class = 'BB'),
	dict(Name = 'Yamato', Laid_down = '1937', Struck = '1945', Class = 'BB'),
	dict(Name = 'Hamakaze', Laid_down = '1939', Struck = '1945', Class = 'DD'),
	dict(Name = 'Kongou', Laid_down = '1911', Struck = '1945', Class = 'BB'),
        dict(Name = 'Akitsumaru', Laid_down = '1941', Struck = '1944', Class = 'LHA'),
        dict(Name = 'Bismarck', Laid_down = '1936', Struck = '1941', Class = 'BB'),
        dict(Name = 'Leberecht Maass', Laid_down = '1934', Struck = '1940', Class = 'DD'),
        dict(Name = 'Max Schultz', Laid_down = '1935', Struck = '1940', Class = 'DD'),
        dict(Name = 'Graf Zeppelin', Laid_down = '1936', Struck = '1947', Class = 'CV'),
        dict(Name = 'Saratoga', Laid_down = '1920', Struck = '1946', Class = 'CV'),
        dict(Name = 'Iowa', Laid_down = '1940', Struck = '2006', Class = 'BB'),
        dict(Name = 'Littorio', Laid_down = '1934', Struck = '1948', Class = 'BB'),
        dict(Name = 'Richelieu', Laid_down = '1935', Struck = '1968', Class = 'BB'),
        dict(Name = 'Gangut', Laid_down = '1909', Struck = '1956', Class = 'BB'),
])

items = open_db('test.db')
for i in items:
    s = i.get('Name')
    print('Name: ', '{:16s}'.format(s),'|',end='')
    s = i.get('Class')
    print('Class: ', '{:5s}'.format(s),'|',end='')
    s = i.get('Laid_down')
    print('Laid down: ', '{:7s}'.format(s),'|',end='')
    s = i.get('Struck')
    print('Struck: ', '{:7s}'.format(s))
print()
choice_show()
print()


