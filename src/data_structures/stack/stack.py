from linked_list.linked_list import LinkedList


class StackOverflowError(Exception):
    pass


class Stack():
    def __init__(self, values=(), max_size=100):
        oversize = 0
        if len(values) > max_size: # will throw type error if max_size is not int
            oversize = len(values)
            values = values[0:max_size]

        self._ll = LinkedList(values)
        #super().__init__(values)
        # but we need to reverse list b/c linkedlist constructs from values by putting value at index 0 at head of list
        self._ll.reverse()

        if not isinstance(max_size, int):
            raise TypeError("The given max_size {} is not valid. max_size must be an integer".format(max_size))
        # throw ValueError if max_size is negative
        if max_size < 0:
            raise ValueError("The given max_size {} is not valid. max_size must be an integer".format(max_size))

        self.max_size = max_size

        if oversize > 0:
            raise StackOverflowError("This stack has a maximum size limit of {0}. Number of intitial values {1} "
                                     "exceeds this limit. Only first {0} values have been pushed".format(max_size, oversize))

    def pop(self):
        """Removes the top element from the stack and returns it"""
        if self._ll.head:
            return self._ll.pop(0)
        raise IndexError("Trying to pop from empty stack")

    def push(self, value):
        """Puts an element on top of the stack. throws StackOverflowError if push will exceed max size"""
        if len(self._ll) == self.max_size:
            raise StackOverflowError("Pushing element {0} will exceed maximum size {1} of this stack".format(value, self.max_size))
        self._ll.insert(0, value)

    def peek(self):
        """ Return a copy of the top element of the stack without removing. Error if stack is empty"""
        if self._ll.head:
            return self._ll.head.value
        raise IndexError("Trying to peek at top value of empty stack")

    def __len__(self):
        return len(self._ll)


def check_balance_paren(expression):
    st = Stack()
    open_parens = ['(', '{', '[']
    close_parens = [')', '}', ']']
    for ch in expression:
        if ch in open_parens:
            st.push(ch)
        elif ch in close_parens and (not len(st) or st.pop() != open_parens[close_parens.index(ch)]):
            return False
    return not len(st)  # if the stack is not empty at the end, not balanced


def main():
    #st = Stack(list(range(10)), max_size=9)
    s = input("Enter an expression to check the balance (Enter to quit): ")
    while (s):
        print("{} is".format(s), "balanced" if check_balance_paren(s) else "not balanced")
        s = input("Enter an expression to check the balance (Enter to quit): ")

    #print(check_balance_paren(""))


if __name__ == "__main__":
    main()