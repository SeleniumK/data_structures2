"""Implement Binary Search Tree."""


class Node(object):
    """Create Node Object. At this point, Node.Value must be a number."""

    def __init__(self, value=None, left_child=None, right_child=None, parent=None):
        """Initialize Node Object."""
        self.value = value
        self._left_child = left_child
        self._right_child = right_child
        if self._left_child is not None:
            self._left_child = None
            self.left_child = left_child
        if self._right_child is not None:
            self._right_child = None
            self.right_child = right_child
        self.parent = parent

    def _depth(self):
        if self.left_child:
            left_depth = self.left_child._depth()
        else:
            left_depth = 0
        if self.right_child:
            right_depth = self.right_child._depth()
        else:
            right_depth = 0
        return 1 + max(left_depth, right_depth)

    def pre_order(self):
        yield self.value
        if self.left_child:
            for item in self.left_child.pre_order():
                yield item
        if self.right_child:
            for item in self.right_child.pre_order():
                yield item

    def in_order(self):
        if self.left_child:
            for item in self.left_child.in_order():
                yield item
        yield self.value
        if self.right_child:
            for item in self.right_child.in_order():
                yield item

    def post_order(self):
        if self.left_child:
            for item in self.left_child.post_order():
                yield item
        if self.right_child:
            for item in self.right_child.post_order():
                yield item
        yield self.value

    @property
    def left_child(self):
        """Mask private left_child."""
        return self._left_child

    @left_child.setter
    def left_child(self, value):
        """Set left_child of node if no current left_child."""
        if isinstance(value, Node) and self._left_child is None:
            self._left_child = value
            value.parent = self
        else:
            raise TypeError

    @property
    def right_child(self):
        """Mask private right_child."""
        return self._right_child

    @right_child.setter
    def right_child(self, value):
        """Set right_child of node if no current right_child."""
        if isinstance(value, Node) and self._right_child is None:
            self._right_child = value
            value.parent = self
        else:
            raise TypeError

    def _breadth_helper(self):
        if self.left_child:
            yield self.left_child.value
        if self.right_child:
            yield self.right_child.value
        if self.left_child:
            for item in self.left_child._breadth_helper():
                yield item
        if self.right_child:
            for item in self.right_child._breadth_helper():
                yield item

class Bst(object):
    """Create a Binary Search Tree Object."""

    def __init__(self, root=None):
        """Initialize Binary Search Tree."""
        self.root = root
        self._size = 0

    def pre_order(self):
        for item in self.root.pre_order():
            yield item

    def in_order(self):
        for item in self.root.in_order():
            yield item

    def post_order(self):
        for item in self.root.post_order():
            yield item

    def breadth_first(self):
        yield self.root.value
        for item in self.root._breadth_helper():
            yield item



    def insert(self, value):
        """Make new node and, if node not in tree, insert into tree."""
        if not isinstance(value, (int, float)):
            raise TypeError
        new_node = Node(value=value)
        self._size += 1
        if self.root is None:
            self.root = new_node
        else:
            cursor = self.root
            while True:
                if cursor.value == new_node.value:
                    return
                elif new_node.value > cursor.value:
                    if cursor.right_child is None:
                        cursor.right_child = new_node
                        return
                    cursor = cursor.right_child
                else:
                    if cursor.left_child is None:
                        cursor.left_child = new_node
                        return
                    cursor = cursor.left_child

    def contains(self, value):
        """Check if node with property equal to value is in tree.

        Return Boolean Value.
        """
        cursor = self.root
        while True:
            if cursor.value == value:
                return True
            elif value > cursor.value:
                if cursor.right_child is None:
                    return False
                cursor = cursor.right_child
            else:
                if cursor.left_child is None:
                    return False
                cursor = cursor.left_child

    def size(self):
        """Return _size property of tree."""
        return self._size

    def depth(self):
        """Return integer representing number of levels in tree."""
        return self.root._depth()

    def balance(self):
        """Return Balance of tree.

        If Right is deeper than left, expect a positive integer.
        Expect a negative integer is left size is deeper than right.
        """
        left_counter = 0
        right_counter = 0
        cursor = self.root

        while cursor.left_child:
            left_counter += 1
            cursor = cursor.left_child

        cursor = self.root

        while cursor.right_child:
            right_counter += 1
            cursor = cursor.right_child

        return right_counter - left_counter
