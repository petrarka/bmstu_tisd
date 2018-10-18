#ifndef IO_H
#define IO_H
#include "err.h"
#include <stdio.h>

#define N 100

int fill_arr(FILE *f, int *pbeg, int **pend);
void print_arr(const int *pb, const int *pe);

#endif // IO_H
