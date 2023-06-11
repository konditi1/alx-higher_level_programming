#include "lists.h"

/**
* reverse_list - Reverses a linked list.
* @head: Double pointer to the head of the linked list.
*/
void reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
}
/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Double pointer to the head of the linked list.
* Return: 1 if the list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev = NULL, *temp = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}
if (fast != NULL)
{
slow = slow->next;
}
reverse_list(&prev);
while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
{
is_palindrome = 0;
break;
}
prev = prev->next;
slow = slow->next;
}
reverse_list(&prev);
temp = prev;
while (temp->next != NULL)
{
temp = temp->next;
}
temp->next = slow;
return (is_palindrome);
}
