from AbstractCollection import AbstractCollection
from LinkedQueue import LinkedQueue
from BinaryNode import BinaryNode


class LinkedBST(AbstractCollection):

	""" A linked version of a binary search tree """
	def __init__(self):
		self._root = None
		AbstractCollection.__init__(self)

# breadth:
#      Create a queue
#      Add root to the queue
#      Loop until queue is empty:
#           print Node at front of queue
#           pop Node from queue
#           add Node’s left and right children to queue
	def bfs_akabreakfast(self):


	# edited code to answer promt 1
	def find(self, item):
		visited_nodes = []
		none_node_visit = []
		""" Returns 'item' if it's found, and 'None' otherwise """
		def recurse(node):
			# Base case 1
			if node is None:

				# if reaches here, not in the tree
				print(f"\nSearch complete, not found. {len(visited_nodes)} Node visited.")
				none_node_visit.append(node)
				return None

			# Base case 2
			elif node.data == item:

				# handles if item is the root, and if in the tree
				if len(visited_nodes) == 0:
					print(f"\nSearch complete, {node.data} found. 0 Node visited")
				else:
					print(f"\nSearch complete, {node.data} found. {len(visited_nodes)} Node visited.")

				return node.data

			elif item < node.data:
				visited_nodes.append(node.data)
				return recurse(node.left)
			else:
				visited_nodes.append(node.data)
				return recurse(node.right)

		return recurse(self._root)

	def height(self):
		""" Returns the current height of the tree """
		def recurse(node):
			# Base case
			if node is None:
				return 0
			return 1 + max(recurse(node.left), recurse(node.right))
		return recurse(self._root)

	# code to answer promt 2
	def height_from_node(self):
		"""
		calls BinaryNode's height method. similar to linkedBST's height method but further down the pipline
		"""
		return BinaryNode.node_height(self._root)

	def inorder(self):

		def recurse(node):
			if node is None:
				return
			recurse(node.left)
			print(node.data, end=" ")
			recurse(node.right)

		recurse(self._root)

	# created to provide visual on tree insertion order
	def preorder(self):

		def recurse(node):
			if node is None:
				return
			print(node.data, end=" ")
			recurse(node.left)
			recurse(node.right)

		recurse(self._root)

	def add(self, item):
		""" Adds 'item' to the binary search tree """

		def recurse(node):
			""" Inner Function to find a new item's location in the tree """
			if item < node.data:
				if node.left is None:
					node.left = BinaryNode(item)
				else:
					recurse(node.left)

			elif item >= node.data:
				if node.right is None:
					node.right = BinaryNode(item)
				else:
					recurse(node.right)

		if self.is_empty():
			self._root = BinaryNode(item)
		else:
			recurse(self._root)

		self._size += 1