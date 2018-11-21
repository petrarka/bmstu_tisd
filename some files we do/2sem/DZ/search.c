#include <stdio.h>
#include <assert.h>
#include "err.h"
#include "io.h"
#include "search.h"

int find_max(const int *b)
{
	int max_dig = 0;
	for (int i = 0; i < BASE; i ++)
		if (b[i] > b[max_dig])
			max_dig = i;
	return max_dig;
}

void upd_table(int *b, int numb)
{
	assert(b != NULL);
	int digit;
	if (numb == 0)
		b[numb] ++;
	while (numb > 0)
	{
		digit = numb % BASE;
		b[digit] ++;
		numb /= 10;
	}
}

int freq_dig(const int *a, int n, int *b)
{
	if (a == NULL || b == NULL)
		return ERR_IO;
	if (n < 0 || n > N)
		return ERR_RANGE;
	for (int i = 0; i < n; i ++)
		upd_table(b,a[i]);
	return OK;
}
