from AbstractCollection import AbstractCollection
from Node import Node


class LinkedQueue(AbstractCollection):

	def __init__(self):
		self._front = None
		self._rear = None
		AbstractCollection.__init__(self)

	def add(self, item):
		""" Adds 'item' to back of queue """
		n = Node(item)
		if self.is_empty():
			self._front = n
		else:
			self._rear.next = n
		self._rear = n
		self._size += 1

	def pop(self):
		""" Removes and returns front item from queue
		Precondition: Queue isn't empty
		Raise: ValueError if Queue is empty
		Postcondition: Queue has one less item """

		if self.is_empty():
			raise ValueError("Queue is empty!")
		return_item = self._front.data
		self._front = self._front.next
		if self._front is None:
			self._rear = None
		self._size -= 1
		return return_item

	def peek(self):
		""" Removes and returns front item from queue
		Precondition: Queue isn't empty
		Raise: ValueError if Queue is empty """

		if self.is_empty():
			raise ValueError("Queue is empty!")
		return self._front.data

	def clear(self):
		""" Make self empty """
		self._front = None
		self._rear = None
		self._size = 0

	def __iter__(self):
		""" Supports iteration over self """
		cursor = self._front
		while cursor is not None:
			yield cursor.data
			cursor = cursor.next