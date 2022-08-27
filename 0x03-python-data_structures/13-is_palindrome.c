#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the node
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *r;
	int *x;
	int len = 0;
	int i = 0;
	int f = 0;
	int a = 0;
 

	r = *head;
	while (r)
	{
		r = (r)->next;
		len++;
	}

	x = malloc(sizeof(int) * (len - 1));
	if (!x)
	{
		free(x);
		return (0);
	}
	if (len <= 1)
		return (1);
	while (len > i && (*head))
	{
		x[i++] = (*head)->n;
		*head = (*head)->next;
	}

	len = len / 2;
	i--;
	while (len > a)
	{
		if (x[a] == x[i])
			f++;
		a++, --i;
	}
	
	if (f == len)
		return (1);
		
	return (0);

}
