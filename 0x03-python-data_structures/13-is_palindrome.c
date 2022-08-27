#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * sparse_pointers - checks if a singly link is pal recursively
 * @h: head of singly list
 * @len: the length of list
 *
 * Return: 1 or 0
 */

listint_t **sparse_pointers(listint_t **h, int len)
{
	int i = 0;
	int k = 0;

	while (len)
	{
		while (i > k)
		{
			h[i] = (h[i])->next;
			k++;
		}
		i++;
		len--;
	}
	return (h);
}

/**
 * check_pal - checks and flags if the same
 * @h: head pointer
 * @len: len of list
 *
 * Return: flag
 */

int check_pal(listint_t **h, int len)
{
	int i = len / 2;
	int flag = 0;
	int j = 0;

	if (i >= 2)
		i++;
	while (i)
	{
		if (((h[j++])->n) == ((h[--len])->n))
			flag++;
		i--;
	}

	return (flag);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the node
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t **p, **q, *r;
	int len = 0;
	int i = 0;
	int f;

	r = *head;
	while (r)
	{
		r = (r)->next;
		len++;
	}

	p = malloc(sizeof(listint_t) * len);
	if (!p)
	{
		free(p);
		return (0);
	}
	if (len <= 1)
		return (1);
	while (len > i)
		p[i++] = *head;
	q = sparse_pointers(p, len);

	f = check_pal(q, len);

	if (f == len / 2)
		return (1);
	return (0);

}

