from time import *
import pickle
import random


### Приветсвие ### 
def greetings():
   greeting = """                     ### Правила игры ###

1.Человек называет любой город.
2.Машина отвечает городом, который оканчивается на последнюю
букву названного города
3.Человек отвечает городом, который оканчивается на последнюю
букву названного города
4.Пункт 2

                     ### Условия проигрыша###
                     
-Если назван несуществующий город
-Если названный город был уже назван
-Если ответ был дан позднее 60 секунд
-Некорректный ввод
                              (｡･ω･｡)
"""
   print(greeting)
   s = input('Введите любое значение для начала')

### Возвращение последней буквы ###
def lastletter(word):
   abc = (' ьъё')
   if word[-1] in abc:
      return word[-2].upper()
   else:
      return word[-1].upper()

### Открытие файла с городами ### 
def open_f(name):
   mass = []
   with open(name,'r') as f:
      text = f.readlines()
      for j in text:
         j = j.strip()
         mass.append(j)
   return mass

### Проверка города ###
def check_city(city):
   k = 0
   name = city[0].upper()+'.txt'
   try:
      citylist = open_f(name)
   except:
      return -1
   for x in citylist:
      if x == city:
         k+=1
         for y in usedcities:
            if x == y:
               return 1
         usedcities.append(city)
         return 0
   if k == 0:
      return -1

### Ответ компьютера ###
def pc_answer(a):
   fl = True
   name = a +'.txt'
   answ_dic = open_f(name)
   lena = len(answ_dic)
   mas1 = []
   k = 0
   while fl or k == lena:
      rndwrd = random.randrange(0,lena-1)
      if rndwrd not in mas1:
         mas1.append(rndwrd)
         k+=1
      if check_city(answ_dic[rndwrd]) == 0:
         fl = False
   if k != lena:
      return answ_dic[rndwrd]
   else:
      return print('You won!!!')


#### Начало программы ####
greetings()
global usedcities
usedcities = []

print()
fl = True
while True:
   if not fl:
      ## Вывод списка использованных городов ##
      print('\nСписок использованных городов:')
      for i in usedcities:
         print(i)
      print()
   t1 = time()
   ## Ответ пользователя ##
   usercity = input('Назовите город: ')
   if usercity == '' or usercity.isspace():
      print('Некорректный ввод')
      break
   t2 = time()
   ## Проверка времени ответа##
   if t2-t1 > 30:
      print('Время истекло')
      try:
         ans = pc_answer(answ)
         print('\nВы могли назвать',ans)
      except:
         pass
      break
   else:
      if fl:
         reslast = usercity[0].upper()
         reslast1 = usercity[0].upper()
         fl = False
      usercity[0].upper()
      result = check_city(usercity)
      ## Проигрыш при ответе города, который был использован ##
      if result == 1:
           print('\nГород уже был использован в Игре.')
           try:
              ans = pc_answer(answ)
              print('\nВы могли назвать',ans)
           except:
              pass
           break
      ## Пользователем дан правильный ответ, компьютер отвечает ##
      if result == 0:
           reslast = usercity[0].upper()
           if reslast == reslast1:
              last = lastletter(usercity)
              resultlast = pc_answer(last)
              reslast1 = lastletter(resultlast).upper()
              answ = resultlast[-1].upper()
              print(resultlast)
           else:
              print('\nНеправильный ответ')
              try:
                 ans = pc_answer(answ)
                 print('\nВы могли назвать',ans)
              except:
                 pass
              break
      ## Проигрыш при ответе города, которого не существует ##
      if result == -1:
           print('\nТакого города не существует.')
           try:
              ans = pc_answer(answ)
              print('\nВы могли назвать',ans)
           except:
              pass
           break

print('Вы проиграли')
print('¯\_(ツ)_/¯')    

