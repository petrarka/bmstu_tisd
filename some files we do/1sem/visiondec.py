word = input('Введите зашифрованное слово ')
key = input("Введите ключ ")
wu = [0]*len(word)
for i in range(len(word)):
    if word[i].isupper():
        wu[i]+=1
        
key = key.lower()
word = word.lower()
abc = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

k = len(key)
lent = len(word)
a = len(abc)
res = []

for i in range(k,lent):
    key = key + key[i%k]
k = len(key)


for i in range(k):
    v1 = abc.find(word[i])
    v2 = abc.find(key[i])
    if word[i].isspace():
        res.append(word[i])
        continue
    if key[i].isspace():
        continue
    if v1<0 or v2<0:
        res.append(word[i])
        continue
    app = abc[(v1-v2)%33]
    res.append(app)


print('Исходное слово ',end = '')
for i in range(len(res)):
    if wu[i]:
        print(res[i].upper(),end='',sep='')
    else:
        print(res[i],end='',sep='')
