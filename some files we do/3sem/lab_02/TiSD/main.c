#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define B_SIZE 128
typedef enum { TECHNICAL, ART, CHILDREN } key;
typedef enum { NATIVE, TRANSLATED } tech_literature;
typedef enum { NOVEL, PIECE } art_literature;
typedef enum { TALE, POETRY } child_literature;

ssize_t my_getline(char **lineptr, size_t *n, FILE *stream)
{
	if (ferror(stream) || feof(stream)) 
		return -1;
	char buf[B_SIZE];
	*n = 0;
	char *string = NULL;
	char *tmp = malloc(*n + B_SIZE + 1);
	if (!tmp)
		return -1;
	
	while(fgets(buf, B_SIZE, stream))
	{
		int len;
		for (len = 0; buf[len] != '\0'; len++);
		
		char *check = realloc(tmp, *n + len + 1);
		if (check)
			tmp = check;
		else
			return -1;
		for (int i = 0; i < *n; i++)
			tmp[i] = string[i];
		if (string)
			free(string);
		
		string = tmp;

		for (int i = 0; i < len+1; i++)
			(string + *n)[i] = buf[i];
			
		*n += len;

		if(string[*n - 1] == '\n')
		{
			string[*n - 1] = '\0';
        	break;
  		}
	}
	
	*lineptr = string;
	return *n;
}

struct Book
{
	char *surname;
	char *title;
	char *publisher;
	key kind;
	
	struct Book *next;
	
    union
    {
        struct
		{
			char *department;
			tech_literature lang;
			int year;
		} technical;
		
		struct
		{
			art_literature genre;
		} art;
		
		struct
		{
			child_literature genre;
		} children;
    } type_literature;
};

struct Book *create_new_book(char *surname, char *title, char *publisher, key kind, char *department, tech_literature lang, int year,
	art_literature genre0, child_literature genre1)
{
	struct Book *b = malloc(sizeof(struct Book));
	if (b)
	{
		b -> surname = surname;
		b -> title = title;
		b -> kind = kind;
		b -> publisher = publisher;
		b -> next = NULL;
		if (kind == TECHNICAL)
		{
			b -> type_literature.technical.department = department;
			b -> type_literature.technical.lang = lang;
			b -> type_literature.technical.year = year;
		}
		else if (kind == ART)
			b -> type_literature.art.genre = genre0;
		else if (kind == CHILDREN)
			b -> type_literature.children.genre = genre1;
	}
	return b;
}

struct Book *add_end(struct Book *head, 
                                   struct Book *b)
{
    struct Book *cur = head;

    if (!head)
        return b;

    for ( ; cur->next; cur = cur->next)
        ;

    cur->next = b;

    return head;
}
	
void print(struct Book *head)
{
    for ( ; head; head = head->next)
	{
		if (head->kind == TECHNICAL)
			printf("%d %s %s %s %s %d %d\n", head->kind, head->surname, head->title, head->publisher, head->type_literature.technical.department,
		head->type_literature.technical.lang, head->type_literature.technical.year);
		else if (head->kind == ART)
			printf("%d %s %s %s %d!\n", head->kind, head->surname, head->title, head->publisher, head -> type_literature.art.genre);
		else if (head->kind == CHILDREN)
			printf("%d %s %s %s %d!!\n", head->kind, head->surname, head->title, head->publisher, head -> type_literature.children.genre);
	}
}

void save(struct Book *head, FILE *f)
{
	for ( ; head; head = head->next)
	{
		if (head->kind == TECHNICAL)
			fprintf(f ,"%d,%s,%s,%s,%s,%d,%d\n", head->kind, head->surname, head->title, head->publisher, head->type_literature.technical.department,
		head->type_literature.technical.lang, head->type_literature.technical.year);
		else if (head->kind == ART)
			fprintf(f ,"%d,%s,%s,%s,%d\n", head->kind, head->surname, head->title, head->publisher, head -> type_literature.art.genre);
		else if (head->kind == CHILDREN)
			fprintf(f ,"%d,%s,%s,%s,%d\n", head->kind, head->surname, head->title, head->publisher, head -> type_literature.children.genre);
	}
}

void load(struct Book **head, FILE *f)
{
	char *str = NULL;
	size_t n = 0;
	while(my_getline(&str, &n, f))
	{
		char *pword = strtok(str, ",");
		int kind = atoi(pword);
		
		pword = strtok(NULL, ",");
		char *s_name = pword;

		pword = strtok(NULL, ",");
		char *titl = pword;
		
		pword = strtok(NULL, ",");
		char *publ = pword;
		if (kind == TECHNICAL)
		{
			pword = strtok(NULL, ",");
			char *dep = pword;
			
			pword = strtok(NULL, ",");
			int langu = atoi(pword);
			
			pword = strtok(NULL, ",");
			int ye = atoi(pword);
			
			struct Book *node = create_new_book(s_name, titl, publ, kind, dep, langu, ye, 0, 0);
			*head = add_end(*head, node);
			str = NULL;
		}
		else if (kind == ART)
		{
			pword = strtok(NULL, ",");
			int a_gen = atoi(pword);
			
			struct Book *node = create_new_book(s_name, titl, publ, kind, NULL, 0, 0, a_gen, 0);
			*head = add_end(*head, node);
			str = NULL;
		}
		else if (kind == CHILDREN)
		{
			pword = strtok(NULL, ",");
			int c_gen = atoi(pword);
			
			struct Book *node = create_new_book(s_name, titl, publ, kind, NULL, 0, 0, 0, c_gen);
			*head = add_end(*head, node);
			str = NULL;
		}
		else
			break;
	}
}

int read_line(char *s, int n)
{
    int ch, i = 0;
    while ((ch = getchar()) != '\n' && ch != EOF)
        if (i < n - 1)
            s[i++] = ch;
    s[i] = '\0';
    return i;
}

int add_el(struct Book **head)
{
	int year, g, k;
	char *sex = malloc(21), *surname = malloc(50), *title = malloc(50), *publisher = malloc(50), *department = malloc(50);
	if (surname == NULL || title == NULL || publisher == NULL || department == NULL)
		return -1;
	gets(sex);
	free(sex);
	printf("Surname of author: ");
	if (!gets(surname))
	{
		puts("K");
		return -1;
	}
	printf("%s",surname);
	printf("Title: ");
	if (scanf("%s",title) != 1)
		return -1;
	printf("Publisher: ");
	if (scanf("%s",publisher) != 1)
		return -1;
	printf("Type of book (0-Technical, 1 - Art, 2 - Children): ");
	if (scanf("%d", &k) != 1 || k < 0 || k > 2)
		return -1;
	if (k == TECHNICAL)
	{
		rewind(stdin);
		printf("Department: ");
		if (scanf("%s",department) != 1)
			return -1;
		printf("Language (0-native, 1 - translated): ");
		if (scanf("%d", &g) == 1)
		{
			if (g > 1 || g < 0)
				return -1;
			printf("Year: ");
			if (scanf ("%d", &year) == 1)
			{
				if (year < 0 || year > 2018)
					return -1;
				struct Book *node = create_new_book(surname, title, publisher, k, department, g, year, 0, 0);
				*head = add_end(*head, node);
				free(surname);
				free(title);
				free(publisher);
				free(department);
			}
			else
				return -1;
		}
		else
			return -1;
	}
	else if (k == ART)
	{
		printf("Type (0-Novel, 1 - Piece): ");
		if (scanf("%d", &g) != 1)
			return -1;
		if (g > 1 || g < 0)
			return -1;
		struct Book *node = create_new_book(surname, title, publisher, k, NULL, 0, 0, g, 0);
		*head = add_end(*head, node);
		free(surname);
		free(title);
		free(publisher);
	}
	else if (k == CHILDREN)
	{
		printf("Type (0 - Fairy tail, 1 - Poetry): ");
		if (scanf("%d", &g) != 1)
			return -1;
		if (g > 1 || g < 0)
			return -1;
		struct Book *node = create_new_book(surname, title, publisher, k, NULL, 0, 0, 0, g);
		*head = add_end(*head, node);
		free(surname);
		free(title);
		free(publisher);
	}
	return 0;
}

int main(void)
{
	setbuf(stdout, NULL);
	struct Book *head = NULL;
	FILE *f;
	f = fopen("bed.bin", "r+b");
	if (f)
	{
		puts("YES");
		load(&head, f);
		fclose(f);
		puts("YES");
	}
	else
		return -1;
	int rc = 0;
	int flag = 1;
	while (flag == 1)
	{
		printf("\n1 - show table\n"
		"2 - add element\n"
		"3 - save to file\n"
		"0 - exit\n"
		"Option: ");
		int k;
		if (scanf("%d",&k) == 1)
		{
			switch(k)
			{
				case 1:
					print(head);
					break;
				case 2:
					rc = add_el(&head);
					print(head);
					if (rc != 0)
						return -1;
					break;
				case 3:
					if (rc == 0)
					{
						f = fopen("bed.bin", "w+b");
						if (f)
						{
							save(head, f);
							printf("Saved");
						}
						else
							return -1;
					}
					break;
				case 0:
					flag = 0;
					break;
			}
		}
		else
			return -1;
	}
	return 0;
}
	/*int k = 1;
	FILE *f;
	f = fopen("bed.bin", "r+b");
	if (f)
	{
		puts("YES");
		load(&head, f);
		fclose(f);
		puts("YES");
	}
	else
		return -1;
	if (scanf("%d",&k) == 1)
	{
		switch(k)
		{
			case 1:
				print(head);
				break;
			case 2:
				rc = add_el(&head);
				if (rc != 0)
					return -1;
				break;
			case 3:
				if (rc == 0)
				{
					f = fopen("bed.bin", "w + b");
					if (f)
					{
						save(head, f);
						printf("Saved");
					}
					else
						return -1;
				}
				break;
	}
	}*/
	/*
	rc = add_el(&head);
	printf("__%d\n",rc);
	print(head);
	if (rc == 0)
	{
		f = fopen("bed.bin", "w + b");
		if (f)
		{
			save(head, f);
			print(head);
		}
		else
			return -1;
	}*/
