"""Implement Binary Search Tree."""
from collections import deque


class Node(object):
    """Create Node Object. At this point, Node.Value must be a number."""

    def __init__(self, value=None, left_child=None, right_child=None, parent=None):
        """Initialize Node Object."""
        self.value = value
        self._left_child = left_child
        self._right_child = right_child
        self.parent = parent

    @property
    def left_child(self):
        """Mask private left_child."""
        return self._left_child

    @left_child.setter
    def left_child(self, value):
        """Set left_child of node if no current left_child."""
        if isinstance(value, Node):
            self._left_child = value
            value.parent = self
        elif value is None:
            self._left_child = value
        else:
            raise TypeError

    @property
    def right_child(self):
        """Mask private right_child."""
        return self._right_child

    @right_child.setter
    def right_child(self, value):
        """Set right_child of node if no current right_child."""
        if isinstance(value, Node):
            self._right_child = value
            value.parent = self
        elif value is None:
            self._right_child = value
        else:
            raise TypeError

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
        """Create Generator for helping Pre order Traversal."""
        yield self.value
        if self.left_child:
            for item in self.left_child.pre_order():
                yield item
        if self.right_child:
            for item in self.right_child.pre_order():
                yield item

    def in_order(self):
        """Create Generator for helping in order Traversal."""
        if self.left_child:
            for item in self.left_child.in_order():
                yield item
        yield self.value
        if self.right_child:
            for item in self.right_child.in_order():
                yield item

    def post_order(self):
        """Create Generator for helping in post order Traversal."""
        if self.left_child:
            for item in self.left_child.post_order():
                yield item
        if self.right_child:
            for item in self.right_child.post_order():
                yield item
        yield self.value


class Bst(object):
    """Create a Binary Search Tree Object."""

    def __init__(self, root=None):
        """Initialize Binary Search Tree."""
        self.root = root
        self._size = 0

    def pre_order(self):
        """Create Generator for in pre order Traversal. Calls Helper."""
        if not self.root:
            return
        for item in self.root.pre_order():
            yield item

    def in_order(self):
        """Create Generator for in in order Traversal. Calls Helper."""
        if not self.root:
            return
        for item in self.root.in_order():
            yield item

    def post_order(self):
        """Create Generator for in post order Traversal. Calls Helper."""
        if not self.root:
            return
        for item in self.root.post_order():
            yield item

    def breadth_first(self):
        """Breadth first traversal."""
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.pop()
            yield node.value
            if node.left_child:
                queue.appendleft(node.left_child)
            if node.right_child:
                queue.appendleft(node.right_child)

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

    def _contains(self, value):
        """Helper function for contains, returns node matching value."""
        cursor = self.root
        if not cursor:
            return False
        while True:
            if cursor.value == value:
                return cursor
            elif value > cursor.value:
                if cursor.right_child is None:
                    return False
                cursor = cursor.right_child
            else:
                if cursor.left_child is None:
                    return False
                cursor = cursor.left_child

    def contains(self, value):
        """Check if node with property equal to value is in tree.

        Calls helper _contains method.
        Return Boolean Value.
        """
        return bool(self._contains(value))

    def size(self):
        """Return _size property of tree."""
        return self._size

    def depth(self):
        """Return integer representing number of levels in tree."""
        return self.root._depth() if self.root else 0

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

        return left_counter - right_counter

    def delete(self, value):
        """Delete node with value given, and adjust tree accordingly."""
        def rebal(list_):
            mid = len(list_) >> 1
            if mid < len(list_):
                yield list_[mid]
                rebal(list_[:mid])
                rebal(list_[mid + 1:])

        if not self.contains(value):
            return
        node = self._contains(value)
        tree = Bst()
        ordered_list = list(node.in_order())
        for to_add in rebal(ordered_list):
            if to_add == value:
                continue
            tree.insert(to_add)
        if node.value == self.root.value:
            self.root = tree.root
            return
        elif node.value > node.parent.value:
            node.parent.right_child = tree.root
        elif node.value < node.parent.value:
            node.parent.left_child = tree.root




