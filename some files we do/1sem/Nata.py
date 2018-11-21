### Поиск ###
def scanno(txt):
    gl = (' аеёиоуыэюя')
    sgl = (' бвгджзйклмнпрстфхчцшщ')
    global sl
    sl = 'Нет'
    slo = ''
    lm = len(slo)
    print()
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            slo = txt[i][j]
            
            if len(slo)>=lm:
                mo = 1
                for k in range(len(slo)-1):
                    if gl.find(slo[k])>0 and gl.find(slo[k+1])>0 or sgl.find(slo[k])>0 and sgl.find(slo[k+1])>0:
                        mo = -1
                        break
                if mo > 0:
                    sl = slo
                    lm = len(slo)
                    mo = 1
    print('\nСамое длинное слово, в котором чередуются гласные и согласные: ',sl)

##### По ширине ###
def sdvig_shir(txt,tex):
    lm = 0
    for l in range (len(txt)):
        if len(txt[l])>lm:
            lm = len(txt[l])

    for i in range(len(txt)):
      cur_len=len(txt[i])
      spaces = txt[i].count(' ')
      if txt[i][cur_len-1]==' ':
        spaces-=1
      for j in range(len(tex[i])):
        if tex[i][j] == ' ':
          need_spaces = int((lm - cur_len) / spaces) + 1
          if (lm - cur_len) % spaces:
            need_spaces += 1
            cur_len += 1
          tex[i][j]=' '*need_spaces
          
    for q in range(len(tex)):
        print()
        for k in range(len(tex[q])):
            print(tex[q][k],end='')

### По центру ###
def sdvig_centa(txt,tex):
    lm = 0
    vr = [0]*len(txt)
    for l in txt:
        if len(l)>lm:
            lm = len(l)
    for l in range(len(txt)):
        v = abs(len(txt[l])-lm)
        v = v//2
        vr[l] = v
    
    for i in range(len(txt)):
        tex[i].append(' '*vr[i])
        tex[i].insert(0,' '*vr[i])
            
    for q in range(len(tex)):
        print()
        for k in range(len(tex[q])):
            print(tex[q][k],end='')

### По правому ###
def sdvig_raito(txt,tex):
    lm = 0
    vr = [0]*len(txt)
    for l in txt:
        if len(l)>lm:
            lm = len(l)
    for l in range(len(txt)):
        v = abs(len(txt[l])-lm)
        v = v
        vr[l] = v
    for i in range(len(txt)):
        tex[i].insert(0,' '*vr[i])
        
    for q in range(len(tex)):
        print()
        for k in range(len(tex[q])):
            print(tex[q][k],end='')
        
### По левому ###
def sdvig_lefto(txt,tex):
    lm = 0
    vr = [0]*len(txt)
    for l in txt:
        if len(l)>lm:
            lm = len(l)
    for l in range(len(txt)):
        v = abs(len(txt[l])-lm)
        v = v
        vr[l] = v
    
    for i in range(len(txt)):
        tex[i].append(' '*vr[i])
            
    for q in range(len(tex)):
        print()
        for k in range(len(tex[q])):
            print(tex[q][k],end='')

### Печать исходного текста ###    
def prinoto(txt):
    print('Исходный текст:')
    for q in range(len(txt)):
        print()
        for k in range(len(txt[q])):
            print(txt[q][k],end='')

### Токен ###
def tokenize(txt):
    pun = (".—,-:';«»!…")
    wrd = ''
    wrds = []
    for c in txt:
        if c.isspace() or pun.find(c)>=0:
            if wrd:
                wrds.append(wrd)
                wrd = ''
            wrds.append(c)
        else:
            wrd += c
    return wrds

### Удаление слова ###
def deleto(txt):
    dele = input('\nВведите слово, которое нужно удалить ')
    print()
    for i in range (len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] == dele:
                txt[i][j]= ''
    print('\nИзмененный текст:')
    for q in range(len(txt)):
        print()
        for k in range(len(txt[q])):
            print(txt[q][k],end='')

### Замена слова ###
def edito(txt):
    ed = input("\nВведите слово, которое нужно заменить ")
    ns = input("Введите слово, на которое нужно заменить ")
    for i in range (len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] == ed:
                txt[i][j]= ns
    print('\nИзмененный текст:')
    for q in range(len(txt)):
        print()
        for k in range(len(txt[q])):
            print(txt[q][k],end='')

### Viborrro  ###
def vibor():
    f = 1
    while f == 1:
        i = input('''\n1. Удалить нужное слово
2. Заменить нужное слово
3. Выравнивание текста по левому краю
4. Выравнивание текста по правому краю
5. Выравнивание текста по центру
6. Выравнивание текста по ширине
Выберите опцию: ''')
        if nu.find(i)>=0:
            f = 3
    return(i)


##########################
####MAIN###
nu = ('123456')
global texuto, text
text =['И затем Ошино Оуги…',
       'Ошино Оуги, та, кто появилась как Камбару Суруги; та, кто изрядно встряхнул ',
       'моё второе полугодие выпускного класса; та, кто бродила по улицам города и дёргала за ',
       'ниточки; та, кто раскрыла всё, что было спрятано между строк; та, кто возродила то, что ',
       'казалось завершённым; та, кто требовала осознания и искупления, самобичевания и ', 
       'молчания; та, что была неустрашима в противостоянии и не боялась конфликтов; та, кто ',
       'насмехалась над людскими попытками сгладить углы; та, кто никому не позволяла ',
       'расслабиться.',
       'Ошино Оуги, та, кто появлялась где бы я ни был, словно моя тень. Та, кто была ',
       'повсюду.',
       'Девушка, которую я мог увидеть, когда бы я этого ни захотел, Ошино Оуги, по ',
       'обвинению в том, что её истинная форма была раскрыта, за преступную фальсификацию ',
       'того, кем она являлась, а также за все формы обмана, в которых она была уличена, словно ',
       'её и не существовало с самого начала, она будет поглощена тем, что физически не ',
       'существует, истинной Тьмой, и будет уничтожена, не оставив и следа.',
       'Её праведность и мои ошибки…',
       'Мои ошибки и её праведность… уничтожат друг друга. Взаимная аннигиляция.',
       'Они исчезнут… Перестанут существовать.',
       'Всё, что она сделала, закончится здесь.',
       'Поэтому, позвольте мне сказать ещё раз. Я бы никогда не поблагодарил её ни при ',
       'каких обстоятельствах, но, раз уж на то пошло, позвольте мне сказать последние слова и ',
       'попрощаться с «собой».',
       'Прощай, Ошино Оуги.',
       'Прощай, моя юность…',]

##text =['Я обернулся.',
##       'Оборачиваясь, я всё не мог понять, кто же говорил — голос незнакомый.Но раньше я его ',
##       'слышал. Да, это раздражающее учителей, похожее на автоответчик, деликатное «не знаю».',
##       '- Не двигайся!',
##       'С этим я догадался, что это Сендзёгахара. Добернувшись я понял и, что она, тщательно ', 
##       'прицелившись, и не теряя ни секунды резко удлинила лезвие канцелярского ножа мне в рот.',
##       'лезвие канцелярского ножа мне в рот.',
##       'Лезвие канцелярского ножа.',
##       'Плотно приставлено к моей левой щеке изнутри.',
##       'Не легко, но в то же время и не плотно лезвие прижималось к внутренней стороне моей щеки.',]

for q in text:
    print(q)
    
texuto = []
for l in range(len(text)):
        text[l]=text[l].lower()
for l in text:
    texuto.append(tokenize(l))

scanno(texuto)
f = 1
fl = 1
z = '1'
while fl ==1:
    if z == '2':
        print('¯\_(ツ)_/¯')
        break
    i = vibor()
    print()       
    i = int(i)
    if i == 1:
        print()
        prinoto(texuto)
        deleto(texuto)
        scanno(texuto)
        
    elif i == 2:
        print()
        prinoto(texuto)
        edito(texuto)
        scanno(texuto)
        
    elif i == 3:
        prinoto(texuto)
        print()
        print('\nИзмененный текст:\n')
        sdvig_lefto(text,texuto)
        print('\nСамое длинное слово, в котором чередуются гласные и согласные: ',sl)
        #scanno(texuto)
        
    elif i == 4:
        prinoto(texuto)
        print()
        print('\nИзмененный текст:')
        sdvig_raito(text,texuto)
        #scanno(texuto)
        print('\nСамое длинное слово, в котором чередуются гласные и согласные: ',sl)
        
    elif i == 5:
        prinoto(texuto)
        print()
        print('\nИзмененный текст:\n')
        sdvig_centa(text,texuto)
        #scanno(texuto)
        print('\nСамое длинное слово, в котором чередуются гласные и согласные: ',sl)
        
    elif i == 6:
        prinoto(texuto)
        print()
        print('\nИзмененный текст:\n')
        sdvig_shir(text,texuto)
        #scanno(texuto)
        print('\nСамое длинное слово, в котором чередуются гласные и согласные: ',sl)
        
    fla = 1
    while fla == 1:
        z = input('''\n1.Повторить
2.Выйти\n''')
        if z == '1' or z == '2':
            fla = -1
    
