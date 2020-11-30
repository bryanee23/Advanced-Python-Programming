from Node import Node

class LinkedList:
	def __init__(self):
		self._head = None

	def __len__(self):
		""" Return the number of Nodes in the list """
		count = 0
		probe = self._head
		while probe is not None:
			count += 1
			probe = probe.next
		return count

	def __eq__(self, other):
		if type(self) != type(other):
			return False
		if len(self) != len(other):
			return False
		probe1 = self._head
		probe2 = other._head
		while probe1 is not None:
			if probe1.data != probe2.data:
				return False
			probe1 = probe1.next
			probe2 = probe2.next
		return True

	def add_to_front(self, data):
		""" Add a new Node to the front of the LinkedList, with 'data' as its data attribute """
		self._head = Node(data, self._head)

	def print_list(self):
		""" Print all the data in this linked list """
		probe = self._head
		while probe is not None:
			print(probe.data, end=" ")
			probe = probe.next


####################################
#### Methods for exam prmopt
####################################
	def add_to_back(self, data):
		""" Add a new Node to the back of the LinkedList """
		if self._head is None:
			self._head = Node(data, self._head)
		else:
			probe = self._head
			while probe.next is not None:
				probe = probe.next
			probe.next = Node(data)

	def __add__(self, other):
		""" combine two lists """
		left_list = self._head
		right_list = other._head
		new_list = LinkedList()

		while left_list is not None:
			new_list.add_to_back(left_list.data)
			left_list = left_list.next

		while right_list is not None:
			new_list.add_to_back(right_list.data)
			right_list = right_list.next

		return new_list


	def __len__(self):
		""" combine two lists """
		probe = self._head
		counter = 0
		while probe is not None:
			counter += 1
			probe = probe.next
		return counter

####################################
####################################
"""
Exam Prompt:

1. Add a method add_to_back to the LinkedList class which t
Add a new Node to the back of the list, takes a single parameter (other than 'self'). This method should add the parameter to a Node which is placed the end of the internal linked list. Make sure to consider corner cases!

2. Overload the + operator for LinkedList by overriding the __add__ method. When two LinkedList objects are the operands of the + operator, a new LinkedList should be returned, containing the data of the left operand, followed by the data of the right operand, in the same order. For example, if the left operand has the values 5, 3, and 7 and the right operand has the values 4, 2, and 1, the LinkedList that is returned should have the values 5, 3, 7, 4, 2, and 1 (in that order). Note: the new LinkedList should be made of new Node objects.

3. To greatly simplify the __len__ method, add an integer attribute to the LinkedList class which tracks how many Nodes are in the list. The __len__ method can then simply return this value.

4. Write a driver program (i.e. in the file Main.py or something similar) which demonstrates the use and testing of these various methods.
"""