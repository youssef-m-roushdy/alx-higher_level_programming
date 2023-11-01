#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Inserts a new node into a sorted linked list.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The value to be inserted into the new node.
 *
 * Return: A pointer to the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;

	if (temp == NULL || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;   
	}
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}