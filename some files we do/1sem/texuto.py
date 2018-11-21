abc = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz")
word = input('Введите строку ')
print('\nИзмененные слова')
word.lower()
last = word[len(word)-1]

if abc.find(last) > 0:
    word+='-'
    
lent = len(word)
a = len(abc)
res = []
m = 0
res1=[]
ri = [0]*len(word)
for i in range(lent):
    v1 = abc.find(word[i])
    if v1 < 0:
        ri[i]+=1
for j in range(len(ri)):
    if ri[j] > 0:
        if word[m:j] == '' and abc.find(word[m:j])<0:
            continue
        res.append(word[m:j])
        m = j+1
for i in res:
    if i == '':
        continue
    else:
        res1.append(i)
        
s1 = []
s2 = []
for i in range(len(res1)):
    for j in range(len(res1[i])):
        s1.append(res1[i][j])
    s1.reverse()
    for l in s1:
        print(l,sep = '',end = '')
    print()
    s1 = []

