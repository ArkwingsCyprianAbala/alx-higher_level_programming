#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *header2 = *head;
	listint_t *aux_ = NULL, *aux_2 = NULL;

	if (*head == NULL || header2->next == NULL)
		return (1);
	while (header2 != NULL)
	{
		add_nodeint(&aux_, header2->n);
		header2 = header2->next;
	}
	aux_2 = aux_;
	while (*head != NULL)
	{
		if ((*head)->n != aux_2->n)
		{
			free_listint(aux_);
			return (0);
		}
		*head = (*head)->next;
		aux_2 = aux_2->next;
	}
	free_listint(aux_);
	return (1);
}
