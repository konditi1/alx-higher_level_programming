#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* reverseList - Reverses a linked list.
* @head: Double pointer to the head of the linked list.
*/
void reverseList(listint_t **head)
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
* compareLists - Compares two linked lists for equality.
* @list1: Pointer to the head of the first linked list.
* @list2: Pointer to the head of the second linked list.
*
* Return: 1 if the lists are equal, 0 otherwise.
*/
int compareLists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n != list2->n)
return (0);

list1 = list1->next;
list2 = list2->next;
}

return (list1 == NULL && list2 == NULL);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Double pointer to the head of the linked list.
*
* Return: 1 if the linked list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
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

prev->next = NULL;
reverseList(&slow);

int is_palindrome = compareLists(*head, slow);

if (mid != NULL)
{
prev->next = mid;
mid->next = slow;
}
else
{
prev->next = slow;
}

return (is_palindrome);
}
