#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define B_SIZE 128
typedef enum { TECHNICAL, ART, CHILDREN } key;
typedef enum { NATIVE, TRANSLATED } tech_literature;
typedef enum { NOVEL, PIECE, POEM} art_literature;
typedef enum { TALE, POETRY } child_literature;

unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );

    return d;
}

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
	unsigned int pages;
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

struct Book *create_new_book(char *surname, char *title, char *publisher, key kind, unsigned int pages, char *department, tech_literature lang, int year,
	art_literature genre0, child_literature genre1)
{
	struct Book *b = malloc(sizeof(struct Book));
	if (b)
	{
		b -> surname = surname;
		b -> title = title;
		b -> kind = kind;
		b -> publisher = publisher;
		b -> pages = pages;
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
	puts("");
	int i = 1;
    for ( ; head; head = head->next)
	{
		printf("Line #%d\n",i);
		i++;
		if (head->kind == TECHNICAL)
		{
			printf("Technical\n");
			printf("'%s' by %s\n", head->title, head->surname);
			printf("Published by %s\n", head->publisher);
			printf("%u pages\n", head->pages);
			printf("Department %s\n", head->type_literature.technical.department);
			printf("Language %s\n", head->type_literature.technical.lang == 1 ? "native" : "translated");
			printf("Year: %d\n", head->type_literature.technical.year);
		}
		else if (head->kind == ART)
		{
			printf("Art\n");
			printf("'%s' by %s\n", head->title, head->surname);
			printf("Published by %s\n", head->publisher);
			printf("%d pages\n", head->pages);
			if (head -> type_literature.art.genre == 0)
				printf("Genre: novel\n");
			else if (head -> type_literature.art.genre == 1)
				printf("Genre: piece\n");
			else
				printf("Genre: poetry\n");
		}
		else if (head->kind == CHILDREN)
		{
			printf("Children\n");
			printf("'%s' by %s\n", head->title, head->surname);
			printf("Published by %s\n", head->publisher);
			printf("%d pages\n", head->pages);
			printf("Genre: %s\n",  head -> type_literature.children.genre == 1 ? "tale" : "poetry");
		}
		puts("");
	}
}

void save(struct Book *head, FILE *f)
{
	for ( ; head; head = head->next)
	{
		if (head->kind == TECHNICAL)
			fprintf(f ,"%d,%s,%s,%s,%u,%s,%d,%d\n", head->kind, head->surname, head->title, head->publisher, head->pages, head->type_literature.technical.department,
		head->type_literature.technical.lang, head->type_literature.technical.year);
		else if (head->kind == ART)
			fprintf(f ,"%d,%s,%s,%s,%u,%d\n", head->kind, head->surname, head->title, head->publisher, head->pages, head -> type_literature.art.genre);
		else if (head->kind == CHILDREN)
			fprintf(f ,"%d,%s,%s,%s,%u,%d\n", head->kind, head->surname, head->title, head->publisher, head->pages, head -> type_literature.children.genre);
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
		
		pword = strtok(NULL, ",");
		unsigned int pages = atoi(pword);
		if (kind == TECHNICAL)
		{
			pword = strtok(NULL, ",");
			char *dep = pword;
			
			pword = strtok(NULL, ",");
			int langu = atoi(pword);
			
			pword = strtok(NULL, ",");
			int ye = atoi(pword);
			struct Book *node = create_new_book(s_name, titl, publ, kind, pages, dep, langu, ye, 0, 0);
			*head = add_end(*head, node);
			str = NULL;
		}
		else if (kind == ART)
		{
			pword = strtok(NULL, ",");
			int a_gen = atoi(pword);
			
			struct Book *node = create_new_book(s_name, titl, publ, kind, pages, NULL, 0, 0, a_gen, 0);
			*head = add_end(*head, node);
			str = NULL;
		}
		else if (kind == CHILDREN)
		{
			pword = strtok(NULL, ",");
			int c_gen = atoi(pword);
			
			struct Book *node = create_new_book(s_name, titl, publ, kind, pages, NULL, 0, 0, 0, c_gen);
			*head = add_end(*head, node);
			str = NULL;
		}
		else
			break;
	}
}

int add_el(struct Book *head)
{
	int year, g, k;
	unsigned int pages;
	char *sex = malloc(21), *surname = malloc(50), *title = malloc(50), *publisher = malloc(50), *department = malloc(50);
	if (surname == NULL || title == NULL || publisher == NULL || department == NULL)
		return -1;
	gets(sex);
	free(sex);
	printf("Surname of author: ");
	if (!gets(surname))
		return -1;
	printf("Title: ");
	if (!gets(title))
		return -1;
	printf("Publisher: ");
	if (!gets(publisher))
		return -1;
	printf("Pages: ");
	if (scanf("%u",&pages) != 1)
		return -1;
	printf("Type of book (0-Technical, 1 - Art, 2 - Children): ");
	if (scanf("%d", &k) != 1 || k < 0 || k > 2)
		return -1;
	if (k == TECHNICAL)
	{
		char *sex = malloc(21);
		gets(sex);
		printf("Department: ");
		free(sex);
		if (!gets(department))
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
				puts(surname);
				struct Book *node = create_new_book(surname, title, publisher, k, pages, department, g, year, 0, 0);
				head = add_end(head, node);
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
		printf("Type (0-Novel, 1 - Piece, 2 - Poetry): ");
		if (scanf("%d", &g) != 1)
			return -1;
		if (g > 2 || g < 0)
			return -1;
		puts(surname);
		struct Book *node = create_new_book(surname, title, publisher, k, pages, NULL, 0, 0, g, 0);
		head = add_end(head, node);
		free(surname);
		free(title);
		free(publisher);
		free(department);
	}
	else if (k == CHILDREN)
	{
		printf("Type (0 - Fairy tail, 1 - Poetry): ");
		if (scanf("%d", &g) != 1)
			return -1;
		if (g > 1 || g < 0)
			return -1;
		puts(surname);
		struct Book *node = create_new_book(surname, title, publisher, k, pages, NULL, 0, 0, 0, g);
		head = add_end(head, node);
		free(surname);
		free(title);
		free(publisher);
		free(department);
	}
	return 0;
}

struct Book* delet_by_id(struct Book *head, int id)
{
	int i = 1;
	struct Book *prev = NULL;
	struct Book *cur;
	for (cur = head; cur; cur = cur->next)
	{
		if (i == id)
		{
			puts("S");
			if (prev)
				prev->next = cur->next;
			else
				head = cur->next;
			free(cur);
			return head;
		}
		prev = cur;
		i++;
	}
	return NULL;
}

int print_by_dep(struct Book *head)
{
	char *dep = malloc(100), *sex = malloc(10);
	printf("Department: ");
	gets(sex);
	if(!gets(dep))
		return -1;
	int flag = 0;
	int i = 1;
	for ( ; head; head = head->next)
		if (head->kind == TECHNICAL && strcmp(dep, head->type_literature.technical.department) == 0)
		{
			puts("");
			flag = 1;
			printf("Line #%d\n",i);
			printf("'%s' by %s\n", head->title, head->surname);
			printf("Published by %s\n", head->publisher);
			printf("%u pages\n", head->pages);
			printf("Department %s\n", head->type_literature.technical.department);
			printf("Language %s\n", head->type_literature.technical.lang == 1 ? "native" : "translated");
			printf("Year: %d\n", head->type_literature.technical.year);
			i++;
		}
	if (flag == 0)
		puts("\nNone");
	return 0;
}

struct Book * sort( struct Book *head )
{
    struct Book *new_root = NULL;
    while (head != NULL)
    {
        struct Book *node = head;
        head = head->next;
        if (new_root == NULL || node->pages < new_root->pages)
        {
            node->next = new_root;
            new_root = node;
        }
        else
        {
            struct Book *current = new_root;
            while (current->next != NULL && !(node->pages < current->next->pages))
                  current = current->next;

            node->next = current->next;
            current->next = node;
        }
    }
    return new_root;
}

struct Book* clear( struct Book *node )
{
    while ( node != NULL )
    {
        struct Book *tmp = node;
        node = node->next;

        free(tmp);
    }

    return node;
}

struct Book *getTail(struct Book *cur) 
{ 
    while (cur != NULL && cur->next != NULL) 
        cur = cur->next; 
    return cur; 
} 

// Partitions the list taking the last element as the pivot 
struct Book *partition(struct Book *head, struct Book *end, 
                       struct Book **newHead, struct Book **newEnd) 
{ 
    struct Book *pivot = end; 
    struct Book *prev = NULL, *cur = head, *tail = pivot; 
  
    // During partition, both the head and end of the list might change 
    // which is updated in the newHead and newEnd variables 
    while (cur != pivot) 
    { 
        if (cur->pages < pivot->pages) 
        { 
            // First node that has a value less than the pivot - becomes 
            // the new head 
            if ((*newHead) == NULL) 
                (*newHead) = cur; 
  
            prev = cur;   
            cur = cur->next; 
        } 
        else // If cur node is greater than pivot 
        { 
            // Move cur node to next of tail, and change tail 
            if (prev) 
                prev->next = cur->next; 
            struct Book *tmp = cur->next; 
            cur->next = NULL; 
            tail->next = cur; 
            tail = cur; 
            cur = tmp; 
        } 
    } 
  
    // If the pivot data is the smallest element in the current list, 
    // pivot becomes the head 
    if ((*newHead) == NULL) 
        (*newHead) = pivot; 
  
    // Update newEnd to the current last node 
    (*newEnd) = tail; 
  
    // Return the pivot node 
    return pivot; 
} 
  
  
//here the sorting happens exclusive of the end node 
struct Book* quickSortRecur(struct Book *head, struct Book *end) 
{ 
    // base condition 
    if (!head || head == end) 
        return head; 
  
    struct Book *newHead = NULL, *newEnd = NULL; 
  
    // Partition the list, newHead and newEnd will be updated 
    // by the partition function 
    struct Book *pivot = partition(head, end, &newHead, &newEnd); 
  
    // If pivot is the smallest element - no need to recur for 
    // the left part. 
    if (newHead != pivot) 
    { 
        // Set the node before the pivot node as NULL 
        struct Book *tmp = newHead; 
        while (tmp->next != pivot) 
            tmp = tmp->next; 
        tmp->next = NULL; 
  
        // Recur for the list before pivot 
        newHead = quickSortRecur(newHead, tmp); 
  
        // Change next of last node of the left half to pivot 
        tmp = getTail(newHead); 
        tmp->next =  pivot; 
    } 
  
    // Recur for the list after the pivot element 
    pivot->next = quickSortRecur(pivot->next, newEnd); 
  
    return newHead; 
} 
  
// The main function for quick sort. This is a wrapper over recursive 
// function quickSortRecur() 
void quickSort(struct Book **headRef) 
{ 
    (*headRef) = quickSortRecur(*headRef, getTail(*headRef)); 
    return; 
} 

void sortList(struct Book *head)
{
    struct Book *i, *j, *temp;

    for (i = head; i != NULL ; i = i->next) // i = i->next
    {
        for (j = head->next; j != NULL; j = j->next) // j = j->next
        {
            if (head->pages < head->next->pages)
            {
                temp = head;
                head = head->next;
                head->next = temp;
            }
        }
    }
}

int main(void)
{
	setbuf(stdout, NULL);
	struct Book *head = NULL;
	FILE *f;
	f = fopen("bed.bin", "r+b");
	if (f)
	{
		load(&head, f);
		fclose(f);
	}
	else
		return -1;
	int rc = 0;
	int flag = 1;
	int id, t1, t2, t12, t22;
	while (flag == 1)
	{
		printf("\n1 - show table\n"
		"2 - add element\n"
		"3 - delete by id\n"
		"4 - buble sort\n"
		"5 - qsort\n"
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
					head = NULL;
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					rc = add_el(head);
					if (rc != 0)
						return -1;
					f = fopen("bed.bin", "w+b");
					if (f)
					{
						save(head, f);
						fclose(f);
					}
					else
						return -1;
					break;
				case 3:
					printf("Enter line number: ");
					if (scanf("%d",&id) == 1)
					{
						delet_by_id(head, id);
						f = fopen("bed.bin", "w+b");
						if (f)
						{
							save(head, f);
							fclose(f);
						}
						else
							return -1;
					}
					else
						return -1;
					break;
				case 4:
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					t1 = tick();
					head = sort(head);
					t2 = tick();
					print(head);
					printf("%d\n",(int)(t2-t1));
					head = NULL;
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					break;
				case 5:
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					t12 = tick();
					quickSort(&head);
					t22 = tick();
					print(head);
					printf("%d\n",(int)(t22-t12));
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					break;
				case 6:
					t1 = tick();
					head = sort(head);
					t2 = tick();
					print(head);
					head = NULL;
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					t12 = tick();
					quickSort(&head);
					t22 = tick();
					print(head);
					printf("bb %d\n",(int)(t2-t1));
					printf("qs %d\n",(int)(t22-t12));
					f = fopen("bed.bin", "r+b");
					if (f)
					{
						load(&head, f);
						fclose(f);
					}
					else
						return -1;
					break;
				case 0:
					flag = 0;
					head = clear(head);
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
