main.exe: io.o search.o main.o
	gcc -o main.exe io.o search.o main.o

test.exe : io.o search.o test.o
	gcc -o test.exe io.o search.o test.o
	
io.o : io.c io.h err.h
	gcc -std=c99 -Wall -Werror -c io.c

search.o: search.c search.h err.h
	gcc -std=c99 -Wall -Werror -c search.c
	
main.o : main.c io.h search.h
	gcc -std=c99 -Wall -Werror -c main.c

test.o : test.c io.h search.h
	gcc -std=c99 -Wall -Werror -c test.c
	
clean :
	rm *.o *.exe