CC := gcc
CFLAGS := -std=c99 -Wall -Werror -pedantic

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

app.exe: main.o
	$(CC) -o app.exe main.o

clean:
	rm *.o *.exe
