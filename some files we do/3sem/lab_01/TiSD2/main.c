#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
#define EQUAL_ONE 1
#define EQUAL_ZERO 2

bool is_equal_int (const int *a, int n, const int *b, int n1)
{
    if (n != n1)
        return false;
    for (int i = 0; i < n; i ++)
        if (a[i] != b[i])
            return false;
    return true;
}

void print(int *a, int n)
{
    for (int i = 0; i < n; i ++)
    {
        printf("%d", a[i]);
    }
}

void reverse(int *a, int n)
{
    for(int i = n; i > 0; i --)
    {
        int temp = a[N-i-1];
        a[N-i-1] = a[n-i];
        a[n-i] = temp;;
    }
}

void char_to_array(char *a, int *n, int sign_flag, int *arr)
{
    printf("\nstring %s\n", a);
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

int get_e_and_point(char *a, int n, int *e_pos, int *point_pos, int *e_flag)
{
    int sign_flag = 0;
    int point_flag = 0;
    *e_flag = 0;
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
        else if ((a[i] == 'E' || a[i] == 'e') && *e_flag == 0)
        {
            *e_flag = 1;
            *e_pos = i;
            break;
        }
        else if (a[i] > '9' || a[i] < '0')
            return ERR_IO;
    }

    if (point_flag != 1 && *e_flag == 1)
        *point_pos = *e_pos;
    else if (point_flag != 1 && *e_flag != 1)
    {
        *point_pos = n;
        *e_pos = n;
    }
    else if (point_flag == 1 && *e_flag != 1)
        *e_pos = n;

    if (*e_pos > 30 && sign_flag == 0 && point_flag == 0)
        return ERR_IO;
    else if (*e_pos > 31 && sign_flag == 1 && point_flag == 0)
        return ERR_IO;
    else if (*e_pos > 31 && sign_flag == 0 && point_flag == 1)
        return ERR_IO;
    else if (*e_pos > 32 && sign_flag == 1 && point_flag == 1)
        return ERR_IO;

    return OK;

}

int get_float(char *a, int *real_arr, int *mantissa_sign, long int *por)
{
    printf("\nEnter real numb: ");
    int rc = OK;
    int point_pos;
    int e_pos = 0, e_flag;
    *mantissa_sign = 0;
    if (gets(a))
    {
        int n = 0;
        while (a[n] != '\0')
            n++;
        rc = get_e_and_point(a, n, &e_pos, &point_pos, &e_flag);
        if (rc == OK)
        {
            *mantissa_sign = 0;
            if (a[0] == '-' || a[0] == '+')
                *mantissa_sign = 1;
            if (a[0] == '+')
                *mantissa_sign = 0;
            if (*mantissa_sign >= 0)
            {
                char_to_array(a, &e_pos, *mantissa_sign, real_arr);
                if (e_flag)
                {
                    int i = n-1;
                    while (i > 0)
                    {
                        if (a[i] == 'e' || a[i] == 'E' || a[i] == '+' || a[i] == '-')
                            break;
                        *por += ((a[i] - '0') * pow(10, n - i- 1));
                        i --;
                    }
                }
                int i = point_pos < e_pos ? 1 : 0 + *mantissa_sign;
                if (a[e_pos + *mantissa_sign + 1 + i] == '-')
                    *por *= (-1);
                *por = *por - (e_pos - point_pos) - (*mantissa_sign);
                if (*por > 99999 || *por < -99999)
                    return ERR_IO;
            }
            else
                return ERR_IO;
        }
        else
            return ERR_IO;
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
    if (sign_flag == 1 && n > 31)
        return ERR_IO;
    if (sign_flag == 0 && n > 30)
        return ERR_IO;
    if (a[0] == '+')
        sign_flag = 0;
    return sign_flag;
}

int get_int(char *a, int *array_of_int, int *integer_sign)
{
    int n = 0;
    printf("Enter integer numb: ");
    *integer_sign = 0;
    if (gets(a))
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

int diff(int *a, int *b, int *res, int n)
{
    if (a == NULL || b == NULL || res == NULL)
        return ERR_IO;
    int eq_flag = 1;
    for(int i = 0; i < n; i ++)
    {
        if (a[i] != b[i] && eq_flag == 1)
            eq_flag = 0;
        if (a[i] - b[i] < 0)
        {
            return NEGATIVE;
        }
        else if (a[i] - b[i] > 0)
            break;
    }

    int f = 0;
    int diff;
    for (int i = n-1; i >= 0; i--)
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

int divis(int *a, int *b, int *res, int n, int *k, int *otv, int *j, int *po)
{
    if (*j >= N-1)
        return OK;
    int ones[N-1] = {0};
    ones[n-1] = 1;
    *k = 0;
    int zeroes[N-1] = {0};
    if (is_equal_int(b, n, zeroes, n))
        return ERR_DIV;
    else if (is_equal_int(b, n, ones, n))
        return EQUAL_ONE;
    else if (is_equal_int(a, n, zeroes, n))
        return EQUAL_ZERO;

    while (diff(a, b, res, n) == POSITIVE)
    {
        (*k) ++;
        int *temp = a;
        a = res;
        res = temp;
    }
    if (is_equal_int(a, n, zeroes, n))
    {

        otv[*j] = *k;
        *po = N - *j;
        (*j) ++;
    }
    else if (diff(a, b, res, n) == NEGATIVE)
    {

        otv[*j] = *k;
        (*j) ++;
        *po = N - *j;
        for(int i = 0; i < n - 1; i++)
        {
            a[i] = a[i+1];
        }
        a[n-1] = 0;
       // print(a,n);
        divis(a, b, res, n, k, otv, j, po);
    }
    else
        {
            otv[*j] = *k;
            (*j) ++;
        }

    if ((*k) > 0)
        return OK;
    else
        return NEGATIVE;
}

void print_ans(int integer_sign, int float_sign, int *otv, int por, int j)
{
    int res_sign = pow((integer_sign - float_sign),2);
    int i;
    for (i = 0; i < N-3; i ++)
        if (otv[i] != 0)
            break;
    printf("\n%d %c0.",j, res_sign ? '-' : '+');
    por += N-1-i - j + 1;
    if (i == 0 && otv[N-3] >= 5)
        otv[N-4]+=1;
    for (; i < N-1; i ++)
        printf("%d",otv[i]);
    printf("e%d",por);
}

int main(int argc, char **argvc)
{
    int rc = OK;
    char string_integer[N], string_real[N+8];
    int array_of_int[N-1] = {0}, array_of_mantissa[N-1] = {0};
    int res[N-1] = {0}, otv[N-1] = {0};
    int e_pos, float_sign, integer_sign;
    int n1 = N-1, po;
    long int por = 0;
    int k = 0, j = 0;
    int n = get_int(string_integer, array_of_int, &integer_sign);
    if (n > 0)
    {
        e_pos = get_float(string_real, array_of_mantissa, &float_sign, &por);
        if (e_pos > 0)
        {
            //int ones[N-1] = {0};
            //ones[n-1] = 1;
            int zeroes[N-1] = {0};
            printf("\n$$ por %ld  int_a$$\n", por);
            //printf("\n$$ i_sign %d mant_a$$\n", integer_sign);
            //printf("\n$$ f_sign %d otv$$\n", float_sign);
            reverse(array_of_int, n);
            //print(array_of_int, n1);
            reverse(array_of_mantissa, e_pos);
            //puts("");
            //print(array_of_mantissa, n1);
            //puts("");
            por *= -1;
            rc = divis(array_of_int, array_of_mantissa, res, n1, &k, otv, &j, &po);
            if (rc == OK)
            {
                reverse(otv, j);
                //puts("");
                //print(otv,n1);

                //printf("\nfirst %d %ld",j, por);

                //printf("\n%d",por);
                print_ans(integer_sign, float_sign, otv, por, j);
            }
            else if (rc == EQUAL_ONE)
            {
                //puts("ONES");
                print(array_of_mantissa, n1);
                puts("");
                print_ans(integer_sign, float_sign, array_of_int, 0, j+1);
            }
            else if (rc == EQUAL_ZERO)
            {
                //puts("ZEROES");
                print(zeroes, n1);
                puts("");
                print_ans(integer_sign, float_sign, zeroes, 0, 2);
            }
            else if (rc == ERR_DIV)
                printf("Dividing by zero\n");
        }
        else
            rc = ERR_IO;
    }
    else
        rc = ERR_IO;
    printf("\nOK%d",rc);
    return rc;
}

//9999999999999999999999999999999
