#include <stdio.h>
#include <assert.h>
#include "err.h"
#include "io.h"

int fill_arr(FILE *f, int *pbeg, int **pend)
{
    int i = 0;
    (*pend)++;
    while(fscanf(f, "%d", pbeg) == 1)
    {
        (pbeg)++;
        (*pend)++;
        i ++;
        if (i >= N)
        {
            (*pend)--;
            return ERR_OVERFLOW;
        }
    }
    (*pend)--;
    return OK;
}


void print_arr(const int *pb, const int *pe)
{
    while (pb < pe)
    {
        printf("%d ", *pb);
        pb ++;
    }
}
