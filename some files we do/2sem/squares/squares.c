https://vk.com/id84771999     		    Виталий Горопашный
https://vk.com/id86448018     		    Евгений Мельцайкин
https://vk.com/id121740309    		    Валерон Носков
https://vk.com/9weallcan      		    Анастасия Эберлинг
https://vk.com/radaksusha
https://vk.com/id161938443    		    Милена Закирова
https://vk.com/id181429044    		    Алёна Карикова
https://vk.com/id182926160     		    Анастасия Серёгина
https://vk.com/deliriumx_yo   		    Анастасия Легостева
https://vk.com/andreyshugaev  		    -----
https://vk.com/vika_ashmarina               Vika Ashmarina
https://vk.com/id245858955                  Наталья Ширко
https://vk.com/angelikamakarovskaya 	    Анжелика Макаровская
https://vk.com/xenia_gn 		    Ксения Гнатовская
https://vk.com/rokusaki 		    Константин Чётатам
https://vk.com/frostunets 		    -----
https://vk.com/id292528715 		    Ксения Пронина
https://vk.com/andrewsputnik 		    Андрей Спутник
https://vk.com/yeahso 			    Дима Масленников
https://vk.com/mwittmannn                   Michael Wittmann
https://vk.com/id340289132 		    Ксения Минаева
https://vk.com/dafuu 			    Daria Moroz
https://vk.com/id434599241 		    Say-I Hate-U
https://vk.com/id441058068 		    Лера Ярославцева
https://vk.com/id458852039 		    Мечеслав Олдридж
https://vk.com/senyasolt 		    Ксения Родина
https://vk.com/id471208397		    Дарья Мороз

/*
Вычисляет площадь прямоугольника.
*/
#include <stdio.h>
#define PI 3.154

float rectsq(int a, int b)
{
    return a * b;
}

float circsq(int r)
{
    return PI * r * r;
}

int main(void)
{
 float a,b;
 float sr;

 float r;
 float sc;

 float s;

 printf("Input a and b:");
 scanf("%f%f",&a,&b);
 printf("Input r:");
 scanf("%f",&r);

 sr = rectsq(a,b);
 sc = circsq(r);
 s = sr + sc;

 printf("Square of rectangle is %8.3f\n", sr);
 printf("Square of circle is %8.3f\n", sc);
 printf("General square is %8.3f\n", s);

 return 0;
}
