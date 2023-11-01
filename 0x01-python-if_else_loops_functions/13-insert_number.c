#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_num;

	new_num = malloc(sizeof(listint_t));
	if (new_num == NULL)
		return (NULL);
	new_num->n = number;

	if (node == NULL || node->n >= number)
	{
		new_num->next = node;
		*head = new_num;
		return (new_num);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_num->next = node->next;
	node->next = new_num;

	return (new_num);
}
