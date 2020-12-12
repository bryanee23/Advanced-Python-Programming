class BinaryNode:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

# code for promt 2
	def node_height(self):
		"""
		:param self: root
		determine the height of a specific node
		returns a number
		"""
		def recurse(self):
			if self is None:
				return 0
			else:
				return 1 + max(recurse(self.left), recurse(self.right))

		return recurse(self)