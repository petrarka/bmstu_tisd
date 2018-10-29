#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N_RAND 100

unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );

    return d;
}

int **allocate_matrix(int n, int m)
{
    if (n <= 0 || m <= 0)
        return NULL;
    int **ptrs, *data;
    ptrs = malloc(n * sizeof(int*));
    if (!ptrs)
        return NULL;
    data = malloc(n * m * sizeof(int));
    if (!data)
    {
        free(ptrs);
        return NULL;
    }

    for (int i = 0; i < n; i++)
        ptrs[i] = data + i * m;

    return ptrs;
}

void free_matrix(int **ptrs, int n)
{
    free(ptrs[0]);
    free(ptrs);
}

void print_matrix(int **p, int n, int m)
{
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < m; j ++)
            printf("%4d ", p[i][j]);
        puts("");
    }
    puts("");
}

void auto_fill(int **matr, int n, int m, int percentage)
{
    int zeroes = (n * m) * percentage / 100;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            matr[i][j] = (rand() % (2*N_RAND) - N_RAND);
    while (zeroes > 0)
    {
        int k = rand() % n;
        int f = rand() % m;
        if (matr[k][f] != 0)
        {
            matr[k][f] = 0;
            zeroes --;
        }
    }
}

int hand_fill(int **matr, int n, int m)
{
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            printf("Matr[%d][%d] = ", i, j);
            if (scanf("%d", &matr[i][j]) != 1)
                return -1;
        }
    return 0;
}

void partition(int **matr, int n, int m, int *A, int *IA, int *JA, int *k)
{
    *k = 0;
    int s = 0;
    for(int i = 0; i < m; i++)
    {
        int flag = 0;
        for (int j = 0; j < n; j++)
        {
            if (matr[j][i])
            {
                A[*k] = matr[j][i];
                IA[*k] = j;
                if (flag == 0)
                {
                    JA[s] = *k;
                    s++;
                    flag = 1;
                }
                *k += 1;
            }
        }
        if (flag == 0)
        {
            JA[s] = -1;
            s++;
        }
    }
    for (int i = 1; i < m; i++)
    {
        if (JA[i] == -1)
            JA[i] = JA[i-1];
    }
	if (JA[0] == -1)
		JA[0] = 0;
	JA[m] = *k ? (*k) : 0;
}

int multiply_matrix(int *JA, int *IA, int *A, int n, int **arr, int *res)
{
	for (int i = 0; i < n; i ++)
	{
		res[i] = 0;
		for (int j = JA[i]; j < JA[i+1]; j ++)
			res[i] += A[j] * arr[0][IA[j]];
	}
	return 0;
}

void partition_vect(int *res, int m, int *A, int *IA, int *JA, int *k)
{
	*k = 0;
    for(int i = 0; i < m; i++)
    {
        if (res[i])
        {
            A[*k] = res[i];
            IA[*k] = 0;
            JA[i] = *k;
            *k += 1;
        }
		else
			JA[i] = -1;
    }
    for (int i = 1; i < m; i++)
		if (JA[i] == -1)
			JA[i] = JA[i-1];
	if (JA[0] == -1)
		JA[0] = 0;
	JA[m] = *k ? (*k) : 0;
}
int multiplication(int **matr1, int **matr2, int *res, int n, int m, int m1)
{

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m1; j++)
        {
            res[j] = 0;
            for (int k = 0; k < m; k++)
                res[j] += matr1[i][k] * matr2[k][j];
        }
    return 0;
}

int main(void)
{
    srand (time(NULL));
    int n, m, m1, k, l;
	long int t1, t2, s1_time = 0;
	setbuf(stdout, NULL);
	int percentage;
	printf("Len of vector: ");
	if (scanf("%d", &m1) != 1)
	{
		puts("Wrong input");
		return -1;
	}
	printf("N, M for matrix: ");
    if (scanf("%d %d", &n, &m) != 2)
	{
		puts("Wrong input");
		return -1;
	}
	if (n != m1)
	{
		puts("Wrong input");
		return -1;
	}
	int A[n*m], IA[n*m], JA[m+1];
	int A1[m], IA1[m], JA1[m+1];
    int **matr = allocate_matrix(n, m);
	int **vect = allocate_matrix(1, m1);
	int *res = malloc(m * sizeof(int));
    if (matr && vect)
    {
		puts("Options:\n"
		"1 - fill by hand\n"
		"2 - fill auto\n"
		"3 - time");
		if (scanf("%d",&l) != 1)
		{
			puts("Wrong input");
			return -1;
		}
		switch(l)
		{
			case 1:
				if (hand_fill(vect, 1, m1) == 0)
				{
					puts("Vector");
					print_matrix(vect, 1, m1);
				}
				else
					{
						puts("Wrong input");
						return -1;
					}
				if (hand_fill(matr, n, m) == 0)
				{
					puts("Matrix");
					print_matrix(matr, n, m);
				}
				else
					{
						puts("Wrong input");
						return -1;
					}
				partition(matr, n, m, A, IA, JA, &k);
				printf(" A: ");
				for (int i = 0; i < k; i++)
					printf("%d ",A[i]);
				puts("");
				printf("IA: ");
				for (int i = 0; i < k; i++)
					printf("%d ",IA[i]);
				puts("");
				printf("JA: ");
				for (int i = 0; i < m+1; i++)
					printf("%d ",JA[i]);
				multiply_matrix(JA, IA, A, m, vect, res);
				if (m1 < 10)
					for (int i = 0; i < m; i ++)
						printf("%d ", res[i]);
				puts("");
				partition_vect(res, m, A1, IA1, JA1, &k);
				printf(" A: ");
				for (int i = 0; i < k; i++)
					printf("%d ",A1[i]);
				puts("");
				printf("IA: ");
				for (int i = 0; i < k; i++)
					printf("%d ",IA1[i]);
				puts("");
				printf("JA: ");
				for (int i = 0; i < m+1; i++)
					printf("%d ",JA1[i]);
				puts("\nResult");
				puts("");
				break;
			case 2:
				printf("Percentage: ");
				if (scanf("%d", &percentage) != 1)
					{
						puts("Wrong input");
						return -1;
					}
				auto_fill(matr, n, m, percentage);
				auto_fill(vect, 1, m1, percentage);
				puts("Vector");
				print_matrix(vect, 1, m1);
				puts("Matrix");
				print_matrix(matr, n, m);
				partition(matr, n, m, A, IA, JA, &k);
				printf(" A: ");
				for (int i = 0; i < k; i++)
					printf("%d ",A[i]);
				puts("");
				printf("IA: ");
				for (int i = 0; i < k; i++)
					printf("%d ",IA[i]);
				puts("");
				printf("JA: ");
				for (int i = 0; i < m+1; i++)
					printf("%d ",JA[i]);
				multiply_matrix(JA, IA, A, m, vect, res);
				partition_vect(res, m, A1, IA1, JA1, &k);
				if (m1 < 10)
					for (int i = 0; i < m; i ++)
						printf("%d ", res[i]);
				puts("");
				printf(" A: ");
				for (int i = 0; i < k; i++)
					printf("%d ",A1[i]);
				puts("");
				printf("IA: ");
				for (int i = 0; i < k; i++)
					printf("%d ",IA1[i]);
				puts("");
				printf("JA: ");
				for (int i = 0; i < m+1; i++)
					printf("%d ",JA1[i]);
				puts("\n\nResult");
				puts("");
				break;
				
			case 3:
				printf("Percentage: ");
				if (scanf("%d", &percentage) != 1)
					{
						puts("Wrong input");
						return -1;
					}
				for (int i = 0; i < 1; i ++)
				{
					auto_fill(matr, n, m, percentage);
					auto_fill(vect, 1, m1, percentage);
					partition(matr, n, m, A, IA, JA, &k);
					t1 = tick();
					multiply_matrix(JA, IA, A, m, vect, res);
					t2 = tick();
					s1_time += (t2 - t1);
				}
				printf("Time: %ld\n", (long int)(s1_time/50));
				for (int i = 0; i < 1; i ++)
				{
					auto_fill(matr, n, m, percentage);
					auto_fill(vect, 1, m1, percentage);
					t1 = tick();
					multiplication(vect, matr, res, 1, m1, m);
					t2 = tick();
					s1_time += (t2 - t1);
				}
				printf("Time: %ld\n", (long int)(s1_time/50));
				break;
		}
    }
    return 0;
}
