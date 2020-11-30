class Array:

    def __init__(self, capacity, fill_value=None):
        """ Capacity is the static size of the array
            Each index in the array is filled with fill_value """
        self.logical_size = []

        self._items = []
        for count in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        """ Returns the length of this array """
        return len(self._items)

    def __str__(self):
        """ Returns a string representation of this array """
        return str(self._items)

    def __iter__(self):
        """ Supports iteration with a for loop """
        return iter(self._items)

    def __getitem__(self, index):
        """ Retrieves the item at 'index' """
        return self._items[index]

    def __setitem__ (self, index, new_item):
        """ set the internal list's index to 'new_item' """
        if new_item == None:
            if self._items[index -1] == None and index >= (len(self._items)):
                raise IndexError("Invalid placement, None types only at end")

        if index > (len(self._items) - 1) or index < 0:
            raise IndexError("Array index out of range")

        self._items[index] = new_item
        # print(self._items)


    def get_logical_size(self):
        temp = []
        for val in self._items:
            if val is not None:
                temp.append(val)
        self.logical_size = temp
        return len(self.logical_size)


    def __eq__(self, other):
        if type(self) is not type(other):
            return False

        for i in range(len(self._items)):
            if self._items[i] is not other._items[i]:
                return False
            if self.logical_size[i] is not other.logical_size[i]:
                return False

        return True
