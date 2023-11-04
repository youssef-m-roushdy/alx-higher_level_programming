#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - Checks if a linked list of integers is a palindrome.
 *
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *current = slow->next;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	listint_t *firstHalf = *head;
	listint_t *secondHalf = prev;

	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
			return (0);
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}
