#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycke in it
 * @list: pointer to the head
 *
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
