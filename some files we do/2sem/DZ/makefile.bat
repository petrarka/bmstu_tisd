gcc -std=c99 -Wall -Werror -c io.c
gcc -std=c99 -Wall -Werror -c search.c
gcc -std=c99 -Wall -Werror -c main.c
gcc -o main.exe io.o search.o main.o