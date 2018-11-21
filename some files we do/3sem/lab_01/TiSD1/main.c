#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#define N 31
#define OK 0
#define ERR_IO -2
#define ERR_RANGE -3
#define NEGATIVE - 1
#define POSITIVE 1
#define BASE 10
#define ERR_DIV -4

bool is_equal_int (const int *a, int n, const int *b, int n1)
{
    if (n != n1)
        return false;
    for (int i = 0; i < n; i ++)
        if (a[i] != b[i])
            return false;
    return true;
}

void reverse(int *a, int n)
{
    for(int i = 0; i < n/2; i ++)
    {
        int temp = a[i];
        a[i] = a[n-i-1];
        a[n-i-1] = temp;
    }
}
void print(int *a, int n)
{
    for (int i = 0; i < n; i ++)
    {
        printf("%d", a[i]);
    }
}

void char_to_array(char *a, int *n, int sign_flag, int *arr)
{
    int i = 0, j = 0;
    while (i < *n)
    {
        if (a[i] == '-' || a[i] == '+' || a[i] == '.')
            i ++;
        else
        {
            arr[j] = a[i] - '0';
            i ++;
            j ++;
        }
    }
    *n = j;
}

int get_e_and_point(char *a, int n, int *e_pos, int *point_pos)
{
    int sign_flag = 0;
    int point_flag = 0;
    int e_flag = 0;
    for (int i = 0; i < n; i++)
    {
        if ((a[i] == '+' || a[i] == '-') && sign_flag == 0)
        {
            sign_flag = 1;
        }
        else if (a[i] == '.' && point_flag == 0)
        {
            point_flag = 1;
            *point_pos = i;
        }
        else if ((a[i] == 'E' || a[i] == 'e') && e_flag == 0)
        {
            e_flag = 1;
            *e_pos = i;
        }
        else if (a[i] > '9' || a[i] < '0')
            return ERR_IO;
    }

    if (e_flag != 1)
        *e_pos = n;
    if (point_flag != 1 && e_flag == 1)
        *point_pos = *e_pos;
    else if (point_flag != 1 && e_flag != 1)
        *point_pos = n;
    return OK;

}

int work_with_mantissa(char *a, int e_pos)
{
    int sign_flag = 0;
    if (a[0] == '-' || a[0] == '+')
        sign_flag = 1;

    if (a[0] == '+')
        sign_flag = 0;
    return sign_flag;
}

int get_float(char *a, int *real_arr, int *mantissa_sign, int *por)
{
    printf("\nEnter real numb: ");
    int rc = OK;
    int point_pos;
    int e_pos;
    *mantissa_sign = 0;
    if (scanf("%s", a) == 1)
    {
        int n = 0;
        while (a[n] != '\0')
            n++;
        rc = get_e_and_point(a, n, &e_pos, &point_pos);
        if (rc == OK)
        {
            *mantissa_sign = work_with_mantissa(a, e_pos);
            if (*mantissa_sign >= 0)
            {
                char_to_array(a, &e_pos, *mantissa_sign, real_arr);
                for (int i = n-1; i > e_pos + (point_pos < e_pos); i --)
                    *por += ((a[i] - '0') * pow(10, n - i-1));
                *por = *por - (e_pos - point_pos);
            }
            else
                rc = ERR_IO;
        }
    }
    return e_pos;
}

int get_sign(char *a, int n)
{
    int sign_flag = 0;
    for (int i = 0; i < n; i++)
    {
        if ((a[i] == '+' || a[i] == '-') && sign_flag == 0 && i == 0)
        {
            sign_flag = 1;
        }
        else if (a[i] > '9' || a[i] < '0')
            return ERR_IO;
    }
    if (a[0] == '+')
        sign_flag = 0;
    return sign_flag;
}

int get_int(char *a, int *array_of_int, int *integer_sign)
{
    int n = 0;
    printf("Enter integer numb: ");
    *integer_sign = 0;
    if (scanf("%s", a) == 1)
    {
        while (a[n] != '\0')
            n++;
        *integer_sign = get_sign(a, n);
        if (*integer_sign < 0)
            return ERR_IO;
        else
            char_to_array(a, &n, *integer_sign, array_of_int);
    }
    return n;
}

void shift(int *a, int *n)
{
    for(int i = (*n) - 1; i < *n; i--)
    {
        a[i] = a[i-1];
    }
}

int diff(int *a, int *n1, int *b, int *n2, int *res, int n3)
{
    if (a == NULL || b == NULL || res == NULL)
        return ERR_IO;
    if (n1 <= 0 || n2 <= 0 || n3 <= 0)
        return ERR_RANGE;
    int eq_flag = 1;
    for(int i = 0; i < *n1; i ++)
    {
        if (a[i] != b[i])
            eq_flag = 0;
        if (a[i] - b[i] < 0)
        {
            //diff(b,n2,a,n1,res,n3);
            return NEGATIVE;
        }
        else if (a[i] - b[i] > 0)
            break;
    }
    if (eq_flag == 1)
        return OK;

    int f = 0;
    int diff;
    for (int i = *n1-1; i >= 0; i--)
    {
        diff = a[i] - b[i];
        if (f == 1)
            diff --;
        if (diff < 0)
        {
            diff += BASE;
            f = 1;
        }
        else
            f = 0;
        res[i] = diff;
    }
    return POSITIVE;
}

int divis(int *a, int *n1, int *b, int *n2, int *res, int n3, int *otv, int *i, int *j, int *c)
{
    if (n1 != n2)
    {
        for (int j = *n1; j > 0; j --)
          {
            a[N - 1 - j] = a[*n1 - j];
          }
        for(int i = 0; i < N-1-*n1; i ++)
            a[i] = 0;

        for (int j = *n2; j > 0; j --)
          {
            b[N - 1 - j] = b[*n2 - j];
          }
        for(int i = 0; i < N-1-*n2; i ++)
            b[i] = 0;
        *n1 = *n2 = N-1;
    }
    int nu[N-1] = {0};
    int on[N-1] = {0};
    on[N-1-1] = 1;

    if(is_equal_int(b, *n1, nu, N-1))
        return ERR_DIV;
    if(is_equal_int(b, *n1, on, N-1))
        return OK;
    (*c) ++;
    if (*c > 30)
        return -1;
    int k = 0;
    while (diff(a, n1, b, n2, res, n3) == POSITIVE)
    {
        for(int i = 0; i < *n1; i ++)
        {
            int temp = a[i];
            a[i] = res[i];
            res[i] = temp;
        }
        k ++;
    }
    if (diff(a, n1, b, n2, res, n3) == OK)
    {
        k ++;
        otv[*i] = k;
        (*i) ++;
    }
    else if (diff(a, n1, b, n2, res, n3) == NEGATIVE)
    {
        for(int i = 0; i < *n1; i ++)
        {
            a[i] = a[i+1];
        }
        a[(*n1)-1] = 0;
        divis(a, n1, b, n2, res, n3, otv, i, j, c);
    }
    else
    {
        otv[*i] = k;
        (*i) ++;
        (*j) ++;
        for(int i = 0; i < *n1; i ++)
        {
            a[i] = a[i+1];
        }
        a[(*n1)-1] = 0;
        if (divis(a, n1, b, n2, res, n3, otv, i, j, c) == ERR_DIV)
            return -1;
    }
    return k;
}
int main(int argc, char **argvc)
{
    int rc = OK;
    char string_integer[N], string_real[N+8];
    int array_of_int[N-1], array_of_mantissa[N-1];
    int e_pos, float_sign, integer_sign;
    int n, por = 0;
    int otv[N-1] = {0};
    int res[N] ={0};
    int i = 0, j = 0, c = 0;
    n = get_int(string_integer, array_of_int, &integer_sign);
    if (n > 0)
    {
        e_pos = get_float(string_real, array_of_mantissa, &float_sign, &por);
        if (e_pos > 0)
        {
            printf("\n$$ por %d  int_a$$\n", por);
            print(array_of_int, n);
            printf("\n$$ i_sign %d mant_a$$\n", integer_sign);
            print(array_of_mantissa, e_pos);
            printf("\n$$ f_sign %d otv$$\n", float_sign);
            int k = 1;
            k = divis(array_of_int, &n, array_of_mantissa, &e_pos, res, N-1, otv, &i, &j, &c);
            if (k > 0)
            {
                printf("%d\n", j);
                //reverse(otv, N-1);
                print(otv, N-1);
            }
            else if (k == OK)
            {
                for (int i = 0; i < N-1; i ++)
                    otv[i] = array_of_int[i];
                //reverse(otv, N-1);
                print(otv, N-1);
            }
            else
            {
                print(otv, N-1);
            }
        }
    }
    else
        rc = ERR_IO;
    printf("\nOK%d",rc);
    return rc;
}

