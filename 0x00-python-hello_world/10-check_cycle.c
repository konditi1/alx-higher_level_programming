#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: pointer to the head of the linked list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *tractor, *car;

if (list == NULL)
return (0);

tractor = list;
car = list->next;

while (car && car->next)
{
if (tractor == car)
return (1);

tractor = tractor->next;
car = car->next->next;
}

return (0);
}
