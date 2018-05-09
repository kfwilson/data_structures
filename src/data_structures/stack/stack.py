from typing import Iterable

from linked_list.linked_list import LinkedList


class StackOverflowError(Exception):
    pass


class Stack(LinkedList):
    def __init__(self, values=(), max_size=100):
        if len(values) > max_size:
            raise StackOverflowError("This stack has a maximum size limit of {0}. Number of intitial values "
                                     "exceeds this limit. Only first {0} values have been pushed".format(max_size))
        super().__init__(values)
        # but we need to reverse list b/c linkedlist constructs from values by putting value at index 0 at head of list
        super().reverse()
        self.max_size = max_size

    def pop(self):
        """Removes the top element from the stack and returns it"""
        if self.head:
            return super().pop(0)
        raise IndexError("Trying to pop from empty stack")


    def push(self, value):
        """Puts an element on top of the stack. throws StackOverflowError if push will exceed max size"""
        if len(self) >= self.max_size - 1:
            raise StackOverflowError("Pushing element {0} will exceed maximum size {1} of this stack".format(value, self.max_size))
        self.insert(0, value)

    def peek(self):
        """ Return a copy of the top element of the stack without removing. Error if stack is empty"""
        if self.head:
            return self.head.value
        raise IndexError("Trying to peek at top value of empty stack")

