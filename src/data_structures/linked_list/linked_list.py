from typing import Iterable

from node import Node


class LinkedListNode(Node):

    def __init__(self, value, next_node=None):
        super().__init__(value)
        self._next = next_node

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        if isinstance(new_next, LinkedListNode) or new_next is None:
            self._next = new_next
        else:
            raise TypeError("The {0}.next must also be an instance of {0}".format(LinkedListNode))

    def __str__(self):
        if self.next:
            return "[{0} | ({1})-]-->".format(self.value, self.next.value)
        else:
            return "[{} | (None)-]-->[None]".format(self.value)


class LinkedList:

    def __init__(self, values=()):
        if isinstance(values, Iterable):
            if values:
                self.head = LinkedListNode(values[0])
                curr = self._head
                for v in values[1:]:
                    curr.next = LinkedListNode(v)
                    curr = curr._next
            else:
                self._head = None
        else:
            raise TypeError("{} object is not iterable.".format(values))

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_head):
        if isinstance(new_head, LinkedListNode) or new_head is None:
            self._head = new_head
        else:
            raise TypeError("The head of a LinkedList can only be a LinkedListNode (or None)")


    def _get(self, index):
        """Private method to return node at passed index"""
        if not isinstance(index, int):
            raise IndexError("The given index {} is not a valid index. Indices must be integers)".format(index))
        if index < 0 or index >= len(self):
            raise IndexError("The given index {0} is not a valid index. Indices must fall in the range [0,{1}]".format(index, len(self)-1))

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr

    def insert(self, index, value):
        """Insert a new node containing value at the given index"""
        if not isinstance(index, int):
            raise IndexError("The given index {} is not a valid index. Indices must be integers)".format(index))

        if not index: # index is 0 so insert at head
            new_node = LinkedListNode(value)
            if self.head:
                new_node.next = self.head
            self.head = new_node
        else:
            prev = self._get(index-1)
            new_node = LinkedListNode(value, next_node=prev.next)
            prev.next = new_node

    def pop(self, index=None):
        """Remove the node at the passed index and return the value it contained"""
        if index is None:
            return self.pop(0)
        if not isinstance(index, int):
            raise IndexError("The given index {} is not a valid index. Indices must be integers)".format(index))

        if not index:
            value = self._get(0).value
            self.head = self.head.next
        else:
            prev = self._get(index-1)
            value = prev.next.value
            prev.next = prev.next.next
        return value

    def print_list(self):
        """Traverse the list and print values. Print message indicating list is empty if no values to print."""
        if self.head is None:
            print("The list is empty.")
        else:
            curr = self.head
            print(curr)
            curr = curr.next
            while (curr is not None):
                print(", " + curr.value)
                curr = curr.next

    def append(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
        else:
            curr = self._get(len(self)-1)
            curr.next = LinkedListNode(value)

    def reverse(self):
        """Reverses order of list in place"""

        prev = self.head
        if prev:
            curr = prev.next
        else: # list is empty
            return

        while curr:
            # keep track of current node's next node because it will be replaced with prev
            temp = curr.next
            # reverse the link between current node and previous node
            curr.next = prev
            # move one down the list
            prev = curr
            curr = temp

        # now that we're at the end, make head the tail
        self.head.next = None
        # set the new head to the old tail (stored in prev at the end of above loop)
        self.head = prev

    def __len__(self):
        num_elems = 0
        curr = self.head
        while curr:
            num_elems += 1
            curr = curr.next
        return num_elems

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

