#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 20
typedef struct node Stack;

struct node
{
    char data;
    Stack *prev;
};

void clear (Stack *list)
{
    while (list)
    {
        Stack *element = list->prev;
        free(list);
        list = element;
    }
}

Stack* push_list (Stack **list, void **adr, int *pushed)
{
    char data;
    printf("Enter characer: ");
    scanf(" %c",&data);
    getchar();
    Stack *element = malloc(sizeof(Stack));
    adr[*pushed] = (void *)element;
    *pushed += 1;
    if (element)
    {
        element->data = data;
        if (list)
        {
            element->prev = *list;
            *list = element;
        }
        else
            element->prev = NULL;
    }
    return element;
}

int pop(Stack **list, char *data, void **adr, int *poped)
{
    if (*list == NULL)
    {
        puts("\nStack is empty!\n");
        return -1;
    }
    *data = (*list)->data;
    Stack *element = *list;
    *list = (*list)->prev;
    adr[*poped] = (void *)element;
    *poped += 1;
    //printf("%p\n",(void *)element);
    free(element);
    return 0;
}

void print_list(Stack *head)
{
    if (head == NULL)
    {
        puts("Stack is empty!\n");
        return;
    }
    printf("STACK ENDS HERE |");
    for ( ; head; head = head->prev)
    {
        printf(" %c |", head->data);
    }
    puts("\n");
}

int process_list(Stack **head, void **adr, int *poped)
{
    if (*head == NULL)
    {
        puts("Stack is empty!\n");
        return -1;
    }
    char element;
    char parenth_stack[MAX_LEN];
    int i = -1;
    //int flag = 2;
    while (*head)
    {
        if (pop(head, &element, adr, poped) != 0)
        {
            puts("ERR");
            return -1;
        }
        if (element == ')' || element == ']' || element == '}')
        {
            i++;
            parenth_stack[i] = element;
        }
        else if (element == '(' || element == '[' || element == '{')
        {
            if (i == -1 || (element == '(' && parenth_stack[i] != ')') ||
        (element == '[' && parenth_stack[i] != ']') || (element == '{' && parenth_stack[i] != '}'))
            {
                puts("\nParentheses are not balanced!");
                return -1;
            }
            else
                i --;
        }
        //printf("%c ",element);
        //flag --;
    }
    if (i == -1)
    {
        puts("\nParentheses are balanced!");
        return 0;
    }
    else
    {
        puts("\nParentheses are not balanced!");
        return -1;
    }
    puts("");
    return 0;
}

/*
Stack* add_front (Stack *head, Stack *element)
{
    element->next = head;
    return element;
}

Stack* input_list(Stack *head)
{
    char s[MAX_LEN];
    printf("Enter your string: ");
    if (fgets(s,MAX_LEN,stdin) == NULL)
        return NULL;
    s[strlen(s)-1] = '\0';
    puts(s);
    for (int i = 0; i < strlen(s); i++)
    {
        Stack *tmp = create_new_element(s[i]);
        if (tmp != NULL)
            head = add_front(head, tmp);
        else
            return NULL;
    }
    return head;
}

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
*/

void print_adr(void **adr, int n)
{
    if (n == 0)
    {
        puts("EMPTY\n");
        return ;
    }
    for (int i = 0; i < n; i ++)
        printf("%p\n", adr[i]);
    puts("");
}

void print_arr(char *begin, char *cur)
{
    if (cur < begin)
    {
        puts("Stack is empty!!\n");
        return ;
    }
    printf("|");
    while (begin <= cur)
    {
        printf(" %c |", *begin);
        begin ++;
    }
    puts(" STACK ENDS HERE\n");
}

int push_arr(char *begin, char *end, char **cur)
{
    char el;
    printf("Enter characer: ");
    scanf(" %c",&el);
    getchar();
    *cur += 1;
    if (*cur + 1 > end)
    {
        *cur = end - 1;
        puts("\nStack is full!!\n");
        return -1;
    }
    **cur = el;
    //printf("_%c_",**cur);
    return 0;
}

int pop_arr(char *begin, char *element, char **cur)
{
    *element = **cur;
    *cur -= 1;
    if (*cur + 1 < begin)
    {
        *cur = begin - 1;
        puts("\nStack is empty!!\n");
        return -1;
    }
    return 0;
}

int process(char *stack, char **head)
{
    if (*head < stack)
    {
        puts("Stack is empty");
        return -1;
    }

    char parenth_stack[MAX_LEN];
    char element;
    int i = -1;
    while (stack <= *head)
    {
        if (pop_arr(stack, &element, head) != 0)
            return -1;
        if (element == ')' || element == ']' || element == '}')
        {
            i++;
            parenth_stack[i] = element;
        }
        else if (element == '(' || element == '[' || element == '{')
        {
            if (i == -1 || (element == '(' && parenth_stack[i] != ')') ||
        (element == '[' && parenth_stack[i] != ']') || (element == '{' && parenth_stack[i] != '}'))
            {
                puts("\nParentheses are not balanced!");
                return -1;
            }
            else
                i --;
        }
        //head --;
    }
    if (i == -1)
    {
        puts("\nParentheses are balanced!");
        return 0;
    }
    else
    {
        puts("\nParentheses are not balanced!");
        return -1;
    }
}

int main (void)
{
    void *pushed_adr[MAX_LEN];
    void *poped_adr[MAX_LEN];
    int pushed = 0, poped = 0;
    setbuf(stdout, NULL);
    char stack_arr[MAX_LEN];
    char *arr_head = stack_arr;
    char *cur = arr_head - 1;
    char *arr_end = stack_arr + MAX_LEN;
    int flag = 1;
    int option1, option;
    char element;
    Stack *head = NULL;
    printf("How to realize your stack?\n"
        "1 - array\n"
        "2 - list\n"
        "Option: ");
    if (scanf("%d", &option1) != 1)
        return -1;
    if (option1 == 1)
    {
        while (flag)
        {
            puts("__________________________________________");
            puts("Stack: ");
            print_arr(arr_head, cur);
            printf("1 - push element\n"
            "2 - pop element\n"
            "3 - check parentheses\n"
            "0 - exit\n"
            "Option: ");
            if (scanf("%d", &option) != 1)
            {
                puts("Wrong input");
                return -1;
            }
            if (option == 1)
            {
                if (push_arr(arr_head, arr_end, &cur) == 0)
                    puts("Pushed!\n");
            }
            else if (option == 2)
            {
                if (pop_arr(arr_head, &element, &cur) == 0)
                    printf("\nElement: %c\n", element);
            }
            else if (option == 3)
                process(arr_head, &cur);
            else if (option == 0)
                flag = 0;
        }
    }
    else if (option1 == 2)
    {
        while (flag)
        {
            puts("__________________________________________");
            puts("Stack: ");
            print_list(head);
            puts("Pushed adresses: ");
            print_adr(pushed_adr, pushed);
            puts("Poped adresses: ");
            print_adr(poped_adr, poped);
            printf("1 - push element\n"
            "2 - pop element\n"
            "3 - check parentheses\n"
            "0 - exit\n"
            "Option: ");
            if (scanf("%d", &option) != 1)
            {
                puts("Wrong input");
                return -1;
            }
            if (option == 1)
            {
                push_list(&head, pushed_adr, &pushed);
            }
            else if (option == 2)
                pop(&head, &element, poped_adr, &poped);
            else if (option == 3)
            {
                process_list(&head, poped_adr, &poped);
                //flag = 0;
            }
            else if (option == 0)
            {
                flag = 0;
                clear(head);
            }
        }
    }
    return 0;
}
