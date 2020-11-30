from arrays import Array
from AbstractStack import AbstractStack


class ArrayStack(AbstractStack):
    """ An array-based stack implementation """

    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection = None):
        """ Sets the initial state of self, which includes contents of source_collection (if present) """

        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self)

    def peek(self):
        """ Returns the item at top of the stack.
        Precondition: The stack is not empty.
        Raises KeyError if the stack is empty """

        # check precondition here
        return self._items[len(self) - 1]

    def push(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __str__(self):
        return "The value at the top of the stack is " + str(self.peek())

    def pop(self):
        """ Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty
        Raises KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack """
        old_item = self._items[len(self) - 1]
        self._size -= 1

        # Resize the array here if necessary
        return old_item
