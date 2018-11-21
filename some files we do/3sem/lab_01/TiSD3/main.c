#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define N 33
#define OK 0
#define ERR_IO -2
#define ERR_RANGE -3
#define NEGATIVE - 1
#define POSITIVE 1
#define BASE 10
#define ERR_DIV -4
#define ERR_OVERFLOW -5
#define EQUAL_ONE 1
#define EQUAL_ZERO 2

//Вывод информации пользователю
void info(void)
{
    puts("This programm can divide integer by float\n"
         "Integer parts length can't be longer than 30\n"
         "Mantissa's length can't be longer than 30\n"
         "Order can't be bigger than 99999 and lower than -99999\n"
         "You can't divide by zero");
}

//Сравнение целочисленных массивов
bool is_equal_int (const int *a, int n, const int *b, int n1)
{
    if (n != n1)
        return false;
    for (int i = 0; i < n; i ++)
        if (a[i] != b[i])
            return false;
    return true;
}

//Вывод массива
void print(int *a, int n)
{
    for (int i = 0; i < n; i ++)
    {
        printf("%d", a[i]);
    }
}

//Перевод массива символов в массив цифр
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

//Получение позиции точки и символа “e” (“E”) с проверкой
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

//Ввод вещественного числа
int get_float(char *a, int *real_arr, int *mantissa_sign, long int *por)
{
    printf("\nEnter float number                 \n");
    printf("1                           30e1   5\n");
    printf("-----------------------------|E|---|\n");
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
                        if (a[i] > '9' || a[i] < '0')
                            return ERR_IO;
                        *por += ((a[i] - '0') * pow(10, n - i- 1));
                        i --;
                    }
                }
                int i = point_pos < e_pos ? 1 : 0 + *mantissa_sign;
                if (a[e_pos + *mantissa_sign + 1 + i] == '-')
                    *por *= (-1);
                *por = *por - (e_pos - point_pos) - (*mantissa_sign);
                if (*por > 99999 || *por < -99999)
                    return ERR_OVERFLOW;
            }
            else
                return ERR_IO;
        }
        else
            return ERR_IO;
    }
    return e_pos;
}

//Получение знака целого числа с проверкой
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

//Ввод целого числа
int get_int(char *a, int *array_of_int, int *integer_sign)
{
    int n = 0;
    printf("\nEnter integer number:         \n");
    printf("1                           30\n");
    printf("-----------------------------|\n");
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

//Вычитание
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

//Сравнение двух чисел, записанных в массив одинаковой длины
int cmp_arr(int *a, int *b, int n1)
{
    for (int i = 0; i < n1; i ++)
    {
        if (a[i] > b[i])
            return 1;
        else if (a[i] < b[i])
            return -1;
    }
    return 0;
}

//Деление
int division(int *a, int *b, int n1, int *otv, long int *por)
{
    int l = 0;
    int zeroes[N-1] = {0};
    if (cmp_arr(b, zeroes, N-1) == 0)
        return ERR_DIV;
    if (cmp_arr(a, zeroes, N-1) == 0)
    {
        for (int i = 0; i < n1; i ++)
            otv[i] = 0;
        return OK;
    }
    int *res = (calloc(N-1, sizeof(int)));
    int j = 0, k = 0;
    while (cmp_arr(a,b, n1) < 0)
    {
        //printf("\n1port %ld\n",*por);
        //print(a, n1);
        //print(b, n1);
        *por -= 1;
        l ++;
        b[l] = b[l-1];
        b[l-1] = 0;
    }
    //puts("$$$$$");
    //print(a, N-3);
    //print(b, N-3);
    while (diff(a,b,res,n1) == POSITIVE)
    {
        int *temp = a;
        a = res;
        res = temp;
        //printf("()()()()()\n");
        //print(a, N-3);
        //print(b, N-3);
        j ++;
        if (cmp_arr(a,zeroes, n1) == 0 || cmp_arr(b,zeroes, n1) == 0)
        {
            otv[k] = j;
            k ++;
            return OK;
        }
        while (cmp_arr(a,b, n1) < 0)
        {
            otv[k] = j;
            k ++;
            j = 0;
            l++;
            b[l] = b[l-1];
            b[l-1] = 0;
        }
        //puts("$$$$$__");
        //print(a, N-3);
        //print(b, N-3);
    }
    free(res);
    return OK;
}

//Округление
void roundarr(int *arr)
{
    int i = N-3;
    if (arr[i] >= 5 && arr[i] != 10)
        arr[i-1] ++;
    //printf("Round %d\n", arr[N-3]);
    while (i > 0)
    {
        if (arr[i] > 9)
        {
            arr[i] = 0;
            arr[i-1] ++;
        }
        i--;
    }

}

//Вывод ответа
void print_ans(int *res, long int por, int integer_sign, int float_sign)
{
    printf("Result: ");
    roundarr(res);
    int res_sign = pow((integer_sign - float_sign),2);
    printf("%c0.", res_sign ? '-' : '+');
    int i = N-2;
    for (; i > 0; i --)
    {
        if (res[i] != 0)
            break;
    }
    //printf("@%d\n",res[i]);
    if (i+1 > N-3)
        print(res, N-3);
    else
        print(res, i+1);
    printf("e%ld",por+1);
}

int main(void)
{
    setbuf(stdout, NULL);
    info();
    int rc = OK;
    char string_integer[N], string_real[N+8];
    int array_of_int[N-1] = {0}, array_of_mantissa[N-1] = {0}, otv[N-1] = {0};
    int e_pos, float_sign, integer_sign;
    int n1 = N-1;//, po;
    long int por = 0;
    int n = get_int(string_integer, array_of_int, &integer_sign);
    if (n > 0)
    {
        e_pos = get_float(string_real, array_of_mantissa, &float_sign, &por);
        if (e_pos > 0)
        {
            //printf("\n%d %d\n", n, e_pos);
            //print(array_of_int, n1);
            puts("");
            //print(array_of_mantissa,n1);
            por = (n - 30) - (e_pos - 30) - por;
            if (por > 99999 || por < -99999)
                rc = ERR_OVERFLOW;
            if (rc == OK)
            {
                rc = division(array_of_int, array_of_mantissa, n1, otv, &por);
                if (rc == OK)
                {
                    printf("\n1st number: %s\n", string_integer);
                    printf("2nd number: %s\n", string_real);
                    print_ans(otv, por, integer_sign, float_sign);
                }
            }
        }
        else if (e_pos == 0)
            rc = ERR_IO;
        else
            rc = e_pos;
    }
    else
        rc = ERR_IO;

    switch(rc)
    {
        case ERR_IO:
        puts("Input/output error");
        break;

        case ERR_RANGE:
        puts("Range error");
        break;

        case ERR_DIV:
        puts("Division error");
        break;

        case ERR_OVERFLOW:
        puts("Overflow!");
        break;
    }
    return rc;
}
