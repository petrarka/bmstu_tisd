#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N_RAND 1000
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
    printf("%d\n",zeroes);
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            matr[i][j] = rand() % N_RAND;
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
    JA[n] = *k ? (*k+1) : 0;
    for (int i = n-1; i > 0; i--)
    {
        if (JA[i-1] == -1)
            JA[i-1] = JA[i];
    }

}

int main(void)
{
    srand (time(NULL));
    int n, m, k;
    int percentage;
    printf("N, M: ");
    if (scanf("%d %d", &n, &m) != 2)
        return -1;
    int **matr = allocate_matrix(n, m);
    if (matr)
    {
        /*if (hand_fill(matr, n, m) == 0)
            print_matrix(matr, n, m);
        else
            return -1;
        int A[n*m], IA[n*m], JA[n+1];
        partition(matr, n, m, A, IA, JA, &k);
        for (int i = 0; i < k; i++)
            printf("%d ",A[i]);
        puts("");
        for (int i = 0; i < k; i++)
            printf("%d ",IA[i]+1);
        puts("");
        for (int i = 0; i < n+1; i++)
            printf("%d ",JA[i]);*/
        printf("Percentage: ");
        if (scanf("%d", &percentage) == 1)
        {
            int A[n*m], IA[n*m], JA[n*m+1];
            auto_fill(matr, n, m, percentage);
            print_matrix(matr, n, m);
            partition(matr, n, m, A, IA, JA, &k);
            printf("A: ");
            for (int i = 0; i < k; i++)
                printf("%d ",A[i]);
            puts("");
            printf("IA: ");
            for (int i = 0; i < k; i++)
                printf("%d ",IA[i]);
            puts("");
            printf("JA: ");
            for (int i = 0; i < n; i++)
                printf("%d ",JA[i] + 1);
            printf("%d\n",JA[n]);
        }
        else
            return -1;
    }
    return 0;
}
