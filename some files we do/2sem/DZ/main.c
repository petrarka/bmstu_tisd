#include <stdio.h>
#include "err.h"
#include "io.h"
#include "search.h"

int main(void)
{
	setbuf(stdout, NULL);
	int a[N], b[BASE];
	int n, max_digit;
	int rc = OK;
	rc = fill_arr(a,&n);
	if (rc == OK)
	{
		rc = freq_dig(a,n,b);
		if (rc == OK)
		{
			max_digit = find_max(b);
			printf("Max digit = %d\n", max_digit);
			print_arr(b,BASE);
		}
		else
			rc == ERR_IO ? puts("Input error!") : puts("0 < n < 100");
	}
	else
		rc == ERR_IO ? puts("Input error!") : puts("0 < n < 100");
	return rc;
}