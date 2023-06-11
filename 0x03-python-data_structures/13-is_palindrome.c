#include "lists.h"
/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Double pointer to the head of the linked list.
* Return: 1 if the linked list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *next = NULL;
listint_t *mid = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast != NULL)
{
mid = slow;
slow = slow->next;
}
next = slow;
prev->next = NULL;

while (next != NULL)
{
next = slow->next;
slow->next = prev;
prev = slow;
slow = next;
}
*head = prev;
fast = *head;

if (mid != NULL)
{
while (fast != NULL && mid != NULL)
{
if (fast->n != mid->n)
return (0);
fast = fast->next;
mid = mid->next;
}
}
return (1);
}
