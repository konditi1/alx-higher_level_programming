#!/usr/bin/python3
"""A class that defines a node of a singly linked list."""


class Node:
    """A class that defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Constructor for the Node class.

        Parameters:
        - data: int
            The data value to be stored in the node.
        - next_node: Node, optional
            The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Parameters:
        - value: int
            The data value to be stored in the node.

        Raises:
        - TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Parameters:
        - value: Node or None
            The next node in the linked list. Can be a Node object or None.

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""
    def __init__(self):
        """Constructor for the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts new Node into correct sorted position in list
        (increasing order).

        Parameters:
        - value: int
            The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - str: A string representing the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
