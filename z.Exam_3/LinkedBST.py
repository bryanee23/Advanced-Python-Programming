from AbstractCollection import AbstractCollection
from LinkedQueue import LinkedQueue
from BinaryNode import BinaryNode


class LinkedBST(AbstractCollection):
    """ A linked version of a binary search tree """

    def __init__(self):
        self._root = None
        AbstractCollection.__init__(self)

    # edited code to answer prompt 1
    def find(self, item):
        visited_nodes = []
        none_node_visit = []
        """ Returns 'item' if it's found, and 'None' otherwise """
        def recurse(node):
            # Base case 1
            if node is None:

                # if reaches here, not in the tree
                print(
                    f"\nSearch complete, not found. {len(visited_nodes)} Node visited.")
                none_node_visit.append(node)
                return None

            # Base case 2
            elif node.data == item:

                # handles if item is the root, and if in the tree
                if len(visited_nodes) == 0:
                    print(
                        f"\nSearch complete, {node.data} found. 0 Node visited")
                else:
                    print(
                        f"\nSearch complete, {node.data} found. {len(visited_nodes)} Node visited.")

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

    # code to answer prompt 2
    def height_from_node(self):
        """
        calls BinaryNode's height method. similar to linkedBST's height method but further down the pipline
        """
        return BinaryNode.node_height(self._root)

		# code to answer prompt 3
    def bfs_akabreakfast(self):
        """
        q = []
        q.add(self.root)
        while q.isempty is not true:
                popped = pop@
                print(pop.q.data)
                q.add(popped.left)
                q.add(popped.pop.right)
        """
        q_silent_ueue = LinkedQueue()
        q_silent_ueue.add(self._root)
        visited = []

        while q_silent_ueue.is_empty is not True:
            popped = q_silent_ueue.pop()

            if popped is not None:
                visited.append(popped.data)
                print(popped.data, end=" ")

                if popped.left is not None:
                    q_silent_ueue.add(popped.left)
                if popped.right is not None:
                    q_silent_ueue.add(popped.right)

            if q_silent_ueue.is_empty():
                break

        # for testing returns array of visited values
        return visited

		# code to answer prompt 4
    def is_balanced(self):
        # handle single node
        if self._root is not None:
            if self._root.left is None and self._root.right is None:
                return True

        q = []
        q.append(self._root)
        while len(q) > 0:
            popped = q.pop(0)

            if popped is not None:
                # handles 3 conditions
                if popped.left is None and popped.right is not None:
                    return False
                elif popped.right is None and popped.left is not None:
                    return False

                else: # left and right node is not none
                    if popped.left is not None:
                        q.append(popped.left)

                    if popped.right is not None:
                        q.append(popped.right)
        return True

    def preorder(self):
        def recurse(node):
            if node is None:
                return
            print(node.data, end=" ")
            recurse(node.left)
            recurse(node.right)
        recurse(self._root)

    def inorder(self):
        def recurse(node):
            if node is None:
                return
            recurse(node.left)
            print(node.data, end=" ")
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
