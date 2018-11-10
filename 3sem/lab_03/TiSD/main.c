#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N_RAND 10

// Info
void info(void)
{
	puts("This programm can multiply row-vector by matrix\n"
	"You can fill matrix by ourself or by computer\n"
	"Also you can compare two methods of multiplication");
}

// Измерение времени
unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );

    return d;
}

// Создание матрицы
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

// Освобождение матрицы
void free_matrix(int **ptrs, int n)
{
    free(ptrs[0]);
    free(ptrs);
}

// Вывод матрицы
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

// Автозаполнение
void auto_fill(int **matr, int n, int m, int percentage)
{
	int tmp;
    long int zeroes = ((n * m) * percentage) / 100;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
		{
			tmp = rand() % (2*N_RAND) - N_RAND;
			while(!tmp)
				tmp = rand() % (2*N_RAND) - N_RAND;
            matr[i][j] = tmp;
		}
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

int hand_fill_vect(int **vect, int n)
{
	int nz, i, num, flag = 1;
	printf("Enter the number of nonzero elements for vector (<= %d): ", n);
	if (scanf("%d",&nz) != 1 || nz > n || nz < 0)
		return -1;
	for (int i = 0; i < n; i ++)
		vect[0][i] = 0;
	puts("Enter index of nonzero element and element for vector");
	while (flag)
	{
		printf("#%d [i] (<%d), element: ", nz, n);
		if (scanf("%d %d", &i, &num) != 2 || i >= n || i < 0 || vect[0][i] != 0 || num == 0)
		{
			puts("NO");
			continue;
		}
		vect[0][i] = num;
		nz --;
		if (nz == 0)
			flag = 0;
	}
	return 0;
}

// Ручное заполнение
int hand_fill(int **matr, int n, int m)
{
	int nz = 0, i, j, num, flag = 1;
	printf("Enter the number of nonzero elements(<=%d): ",n*m);
	if (scanf("%d",&nz) != 1 || nz > n*m || nz < 0)
		return -1;
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j++)
			matr[i][j] = 0;
	puts("Enter row and column of nonzero elements and elements for matrix");
	while (flag)
	{
		printf("#%d [i] (<%d), [j](<%d), element: ",nz, n, m);
		if (scanf("%d %d %d", &i, &j, &num) != 3 || i >= n || j >= m || i < 0 || j < 0 || matr[i][j] != 0 || num == 0)
		{
			puts("NO");
			continue;
		}
		matr[i][j] = num;
		nz --;
		if (nz == 0)
			flag = 0;
	}
    return 0;
}

// Разбиение матрицы на 3 вектора
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

// Умножение вектора на матрицу особым методом
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

// Разбиение вектора на 3 массива
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
	if (JA[0] == -1)
		JA[0] = 0;
    for (int i = 1; i < m; i++)
		if (JA[i] == -1)
			JA[i] = JA[i-1];
	JA[m] = *k ? (*k) : 0;
}

// Умножение вектора на матрицу обычным методом
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
	info();
    int n, m, m1, k, l;
	long int t1, t2, k_sum = 0, s1_time = 0, s2_time = 0, p_sum = 0, mem1 = 0, mem2 = 0;
	setbuf(stdout, NULL);
	int percentage;
	printf("\nLength of vector: ");
	if (scanf("%d", &m1) != 1)
	{
		puts("Wrong input");
		return -1;
	}
	printf("Rows (must be equal to length of vector) and columns for matrix\n N, M: ");
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
		printf("Menu:\n"
		"1 - multiplication, fill with hand\n"
		"2 - multiplication, fill auto\n"
		"3 - time\n"
		"Option: ");
		if (scanf("%d",&l) != 1)
		{
			puts("Wrong input");
			return -1;
		}
		switch(l)
		{
			case 1:
				printf("\nVector\n");
				if (hand_fill_vect(vect, m1) != 0)
				{
					puts("Wrong input");
					return -1;
				}
				puts("\nMatrix");
				if (hand_fill(matr, n, m) != 0)
				{
					puts("Wrong input");
					return -1;
				}
				if (m1 <= 10)
				{
					puts("Vector");
					print_matrix(vect, 1, m1);
					puts("Matrix");
					print_matrix(matr, n, m);
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
				partition_vect(res, m, A1, IA1, JA1, &k);
				puts("\n\nResult");
				if (m1 < 10)
					for (int i = 0; i < m; i ++)
						printf("%d ", res[i]);
				puts("");
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
				puts("");
				break;
			case 2:
				printf("Percentage of sparsity: ");
				if (scanf("%d", &percentage) != 1 || percentage > 100 || percentage < 0)
				{
					puts("Wrong input");
					return -1;
				}
				auto_fill(matr, n, m, percentage);
				auto_fill(vect, 1, m1, percentage);
				if (m1 <= 10)
				{
					puts("Vector");
					print_matrix(vect, 1, m1);
					puts("Matrix");
					print_matrix(matr, n, m);
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
				partition_vect(res, m, A1, IA1, JA1, &k);
				puts("\n\nResult");
				puts("");
				if (m1 <= 10)
					for (int i = 0; i < m; i ++)
						printf("%d ", res[i]);
				puts("");
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
				break;
				
			case 3:
				printf("Percentage of sparsity: ");
				if (scanf("%d", &percentage) != 1 || percentage > 100 || percentage < 0)
					{
						puts("Wrong input");
						return -1;
					}
				s1_time = 0;
				for (int i = 0; i < 50; i ++)
				{
					auto_fill(matr, n, m, percentage);
					auto_fill(vect, 1, m1, percentage);
					partition(matr, n, m, A, IA, JA, &k);
					t1 = tick();
					multiply_matrix(JA, IA, A, m, vect, res);
					t2 = tick();
					k_sum += k;
					for (int i = 0; i < m; i ++)
						if (res[i])
							p_sum ++;
					s1_time += (t2 - t1);
				}
				printf("\nMultiplication time (special method): %ld\n", (long int)(s1_time/50));
				s1_time = s1_time/50;
				mem1 = (long)((sizeof(int)) * (2 * (k_sum/50) + (m+1) + \
				2 * (p_sum/50) + (m+1) + k_sum/50 * 3 + (m+1)));
				printf("Memory: %ld\n", mem1);
				for (int i = 0; i < 50; i ++)
				{
					auto_fill(matr, n, m, percentage-1);
					auto_fill(vect, 1, m1, percentage-1);
					t1 = tick();
					multiplication(vect, matr, res, 1, m1, m);
					t2 = tick();
					s2_time += (t2 - t1);
				}
				printf("\nMultiplication time (standart method): %ld\n", (long int)(s2_time/50));
				s2_time = s2_time/50;
				mem2 = (long)(sizeof(int) * ((m1 * n) + m + m1));
				printf("Memory: %ld\n", mem2);
				
				if (s1_time > s2_time)
					printf("\nStandart method is faster than special method in %4.3lf percent\n", ((double)(s1_time - s2_time) / s1_time) * 100);
				else
					printf("Special method is faster than standart method in %4.3lf percent\n", ((double)(s2_time - s1_time) / s2_time) * 100);
				
				if (mem1 > mem2)
					printf("Standart method takes %4.3lf percent less memory than special method\n", ((double)(mem1 - mem2) / mem1) * 100);
				else
					printf("Special method takes %4.3lf percent less memory than standart method\n", ((double)(mem2 - mem1) / mem2) * 100);
				
				break;
		}
    }
    return 0;
}
