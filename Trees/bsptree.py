#
# Name: SOHAYIB SAZID FAHIM
# Student ID: 202148771
#

# COMP 2002 - Assignment 2
# Terrence Tricco
# September 2022

#from tree_visualizer import visualize_tree

class BSPTree():

    class _Node():

        def __init__(self, parent=None, left=None, right=None, position=None,
                     value=None, length=(0.0, 1.0)):
            """
            Do not modify the constructor.
            """
            self._parent = parent
            self._left = left
            self._right = right
            self._length = length
            self._position = position
            self._value = value
            self._size = 0
            if self._position is not None:
                self._size = 1

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, parent):
            self._parent = parent

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, left):
            self._left = left

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, right):
            self._right = right

        @property
        def length(self):
            return self._length

        @length.setter
        def length(self, length):
            self._length = length

        @property
        def size(self):
            return self._size

        @size.setter
        def size(self, size):
            self._size = size

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self, position):
            self._position = position

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value


        def is_external(self):
            return self.left == None and self.right == None

        # TO DO - Question 1
        def height(self):
            """
            Returns the height of the subtree rooted at this node.
            """
            return self.height


    def __init__(self):
        """
        Do not modify the constructor.
        """
        self._root = None
        self._size = 0

    def _split_node(self, node):
        """
        Creates a child for the node containing its point.
        """
        midpoint = (node.length[1] + node.length[0]) / 2.0
        child = self._Node(parent=node, position=node.position, value=node.value)

        if node.position > midpoint:
            child.length = (midpoint, node.length[1])
            node.right = child
        else:
            child.length = (node.length[0], midpoint)
            node.left = child

    # TO DO - Question 4
    def insert_point(self, pos, value):
        """
        Insert a new point into the tree.

        Walk the tree node by node to find where the new point should be
        inserted.

        There are four possible cases while walking.
        1. The node has two children. Insert the appropriate child node onto
           the stack.
        2. The node does not have children. Made a child for the existing
           point, and re-insert the node onto the stack.
        3. The node has one child and it encloses the new point. Insert the
           child onto the stack.
        4. The node has one child and it does not enclose the new point. Make
           the sibling node for the new point and finish.
        """
        if self._root == None:
            self._root = self._Node(position=pos, value=value)
        else:
            # walk the tree
            stack = [self._root]
            while len(stack) > 0:
                # print(counter)
                curr = stack.pop()
                midpoint = (curr.length[1] + curr.length[0]) / 2.0

                if curr.is_external():
                    self._split_node(curr)
                    stack.append(curr)
                else:
                    # this node is an ancestor; increment size
                    curr.size += 1

                    # avg_pos = curr + abs((pos-curr))/self.leaf()
                    # avg_val = curr + abs((value-curr))/self.leaf()

                    if pos > midpoint and curr._right is None:
                        # pos = curr + abs((pos - curr) / self.leaf())
                        # value = curr + abs((value - curr) / self.leaf())

                        node = self._Node(parent=curr, position=pos, value=value,
                                          length=(midpoint, curr.length[1]))
                        curr.right = node
                        #if node is not curr.is_external():
                            #pos =

                    elif pos < midpoint and curr._left is None:
                        pos = curr + abs((pos - curr) / self.leaf())
                        value = curr + abs((value - curr) / self.leaf())
                        node = self._Node(parent=curr, position=pos, value=value,
                                          length=(curr.length[0], midpoint))
                        curr.left = node
                    else:
                        stack.append(curr.left) if pos < midpoint else stack.append(curr.right)


    # TO DO - Question 1
    def height(self):
        """
        Returns the height of the tree.
        """
        if self._root != None:
            return self._height(self._root, 0) - 1
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    # TO DO - Question 2
    def node_count(self):
        """
        Returns a count of all nodes in the tree.
        """
        # return 2** self.height() - 1   # for total nodes in the tree
        if self._root != None:
            return self._count(self._root)
        else:
            return 0

    def _count(self, cur_node):
        if cur_node is None:
            return 0
        return 1 + self._count(cur_node.left) + self._count(cur_node.right)

    def leaf(self):
        if self._root != None:
            return self._leaf(self._root)
        else:
            return 0

    def _leaf(self, cur_node):
        if cur_node is None:
            return 0
        return self._leaf(cur_node.left)+ self._leaf(cur_node.right)

    # TO DO - Question 3
    def contains(self, pos):
        """
        Returns True if the tree contains a data point at the specified
        position, else returns False.
        """
        if self._root == None:
            return False
        else:
            currentNode = self._root
            if pos > currentNode.length[1] or pos < currentNode.length[0]:
                return False

            while not currentNode.is_external:
                if pos <= currentNode.left.length[1]:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right

                if pos == currentNode.position:
                    if currentNode.value:
                        return True
                    else:
                        return False
                if currentNode == None:
                    return False
                

