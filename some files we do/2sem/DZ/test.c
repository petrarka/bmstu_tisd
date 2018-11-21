#include <stdio.h>
#include "err.h"
#include "io.h"
#include "search.h"
#include <stdbool.h>
#define ARR_SIZE(a) (sizeof(a) / sizeof(a[0]))

bool is_equal (const int *a, const int *b)
{
	for (int i = 0; i < BASE; i ++)
		if (a[i] != b[i])
			return false;
	return true;
}

void test_search(void)
{
	{
		printf("TEST1:");
		int a[] = {0, 3, 4, 1, 2, 3, 0, 0, 0, 0};
		if (find_max(a) == 2)
			puts("OK");
		else
			puts("FAIL");
	}
	
	{
		printf("TEST2:");
		int num = 100489;
		int a[] = {3, 2, 2, 2, 3, 1, 1, 1, 2, 2};
		int b[] = {1, 1, 2, 2, 2, 1, 1, 1, 1, 1};
		upd_table(b, num);
		if (is_equal(a,b))
			puts("OK");
		else
			puts("FAIL");
	}
	
	{
		printf("TEST3:");
		int b1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		int b[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
		freq_dig(a,ARR_SIZE(a),b1);
		if (is_equal(b,b1))
			puts("OK");
		else
			puts("FAIL");
		
	}
	
	{
		printf("TEST4:");
		int b1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int *a = NULL;
		if (freq_dig(a,ARR_SIZE(a),b1) == ERR_IO)
			puts("OK");
		else
			puts("FAIL");
	}
	
	{
		printf("TEST5:");
		int b1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		if (freq_dig(a,-10,b1) == ERR_RANGE)
			puts("OK");
		else
			puts("FAIL");
	}
	
	{
		printf("TEST6:");
		int b1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		if (freq_dig(a,500,b1) == ERR_RANGE)
			puts("OK");
		else
			puts("FAIL");
	}
	
	{
		printf("TEST7:");
		int b1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		if (freq_dig(a,ARR_SIZE(a),b1) == OK)
			puts("OK");
		else
			puts("FAIL");
	}
}

int main(void)
{
    test_search();
    return OK;
}
