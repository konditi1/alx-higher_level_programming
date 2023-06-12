#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)  /* odd number of nodes */
        slow = slow->next;

    prev->next = NULL;  /* disconnect the first half from the second half */
    listint_t *second_half = reverse_list(slow);

    listint_t *temp1 = *head;
    listint_t *temp2 = second_half;

    int is_palindrome = 1;

    while (temp1 != NULL && temp2 != NULL)
    {
        if (temp1->n != temp2->n)
        {
            is_palindrome = 0;
            break;
        }

        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    second_half = reverse_list(second_half);  /* restore the original list */
    prev->next = second_half;  /* reconnect the first half with the second half */

    return (is_palindrome);
}

