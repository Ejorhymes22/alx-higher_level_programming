#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the linked list
 * @number: value of the node
 *
 * Return: address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *it, *current, *node, *temp;
	int k = 0;

	node = malloc(sizeof(listint_t));
	if (!node)
	{
		free(node);
		return (NULL);
	}
	node->n = number;

	if (!(*head))
	{
		*head = node;
		node->next = NULL;
		return (*head);
	}
	current = *head;
	it = current;

	while (number > current->n && current->next)
	{
		it = current;
		current = current->next;
		k++;
	}	
	if (k == 0)
	{
		*head = node;
		node->next = current->next;
		return (node);
	}

	if (!(current->next))
	{
		temp = current->next;
		current->next = node;
		node->next = temp;
		return (node);
	}
	temp = it->next;
	it->next = node;
	node->next = temp;

	return (node);
}
