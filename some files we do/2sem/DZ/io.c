#include <stdio.h>
#include "err.h"
#include "io.h"

void print_arr(const int *a, int n)
{
	for (int i = 0; i < n; i++)
		printf("%d ",a[i]);
	puts("");
}

int fill_arr(int *a, int *n)
{
    printf("Enter the number of numbers: ");
    if (scanf("%d", n) != 1)
        return ERR_IO;
    if (!(*n > 0 && *n <=  N))
        return ERR_RANGE;
    printf("Enter the array: ");
    for (int i = 0; i < *n; i++)
		if (scanf("%d", &a[i]) != 1)
			return ERR_IO;
    return OK;
}