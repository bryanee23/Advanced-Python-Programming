class AbstractCollection:

    def __init__(self, source_collection=None):
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __len__(self):
        return self._size

    def is_empty(self):
        """ Returns True if len(self) == 0, or False otherwise """
        return len(self) == 0

    def __add__(self, other):
        """ Returns a new collection with the contents of 'self' and 'other' """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
