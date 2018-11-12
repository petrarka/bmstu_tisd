#include <string.h>
#include <stdio.h>
#define MAX_LEN 100
typedef struct node Stack;

struct node
{
    char sym;
    Stack *next;
};

int push_arr(char *stack, char **head, char elem)
{
    if ((*head - stack) >= MAX_LEN)
    {
        puts("Stack is full");
        return -1;
    }

    **head = elem;
    *head += 1;
    return 0;
}

int pop_arr(char *stack, char **head)
{
    if ((*head-1) < stack)
    {
        puts("Stack is empty");
        return -1;
    }

    if ((*head - stack) >= MAX_LEN)
    {
        puts("Stack is full");
        return -1;
    }
    *head -= 1;
    return 0;
}

int print_arr(char *stack, char *head)
{
    if ((head-1) < stack)
    {
        puts("Stack is empty");
        return -1;
    }
    while (stack < head--)
        printf("%c ",*(head));
    puts("");
    return 0;
}

/*
Проблема
([)]
*/
int process(char *stack, char *head)
{
    if ((head-1) < stack)
    {
        puts("Stack is empty");
        return -1;
    }
    int cir_op = 0, cir_cl = 0;
    int rec_op = 0, rec_cl = 0;
    int fig_op = 0, fig_cl = 0;
    while (stack < head--)
    {
        if (*(head) == '(')
        {
            cir_op ++;
        }
        else if (*(head) == ')')
        {
            cir_cl ++;
        }
        if (cir_op > cir_cl)
        {
            puts("EnD");
            return -1;
        }

        if (*(head) == '{')
        {
            fig_op ++;
        }
        else if (*(head) == '}')
        {
            fig_cl ++;
        }
        if (fig_op > fig_cl)
        {
            puts("EnD");
            return -1;
        }

        if (*(head) == '[')
        {
            rec_op ++;
        }
        else if (*(head) == ']')
        {
            rec_cl ++;
        }
        if (rec_op > rec_cl)
        {
            puts("EnD");
            return -1;
        }
    }
    if (rec_cl != rec_op)
    {
        puts("End");
        return -1;
    }
    if (fig_cl != fig_op)
    {
        puts("End");
        return -1;
    }
    if (cir_cl != cir_op)
    {
        puts("End");
        return -1;
    }
    printf("%d %d\n",fig_op, fig_cl);
    printf("%d %d\n",rec_op, rec_cl);
    printf("%d %d\n",cir_op, cir_cl);
    return 0;
}

int input_arr (char *stack, char **head)
{
    puts("SD");
    char s[MAX_LEN];
    printf("Enter your string: ");
    if (fgets(s,MAX_LEN,stdin) == NULL)
        return -1;
    s[strlen(s) - 1] = '\0';
    for(int i = 0; i < strlen(s); i ++)
    {
        if (push_arr(stack, head, s[i]) != 0)
            return -1;
    }
    return 0;
}

int main (void)
{
    setbuf(stdout, NULL);
    //Stack *head = NULL;
    char stack_arr[MAX_LEN];
    char *arr_head = stack_arr;
    input_arr(stack_arr, &arr_head);
    //print_arr(stack_arr, arr_head);
    process(stack_arr, arr_head);
    /*push_arr(stack_arr, &arr_head, 's');
    push_arr(stack_arr, &arr_head, 'o');
    push_arr(stack_arr, &arr_head, 'e');
    print_arr(stack_arr, arr_head);
    pop_arr(stack_arr, &arr_head);*/
    return 0;
}
