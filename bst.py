"""Implement Binary Search Tree."""
from collections import deque
import random


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

    def leftest(self):
        if self.left_child:
            return self.left_child.leftest()
        else:
            return self

    def rightest(self):
        if self.right_child:
            return self.right_child.rightest()
        else:
            return self

    def orphan_self(self, child_node):
        """Connects given child to the parent of this node, on the correct side."""
        if self.value == self.parent.value:
            if self.parent.right_child.value == self.value:
                self.parent.right_child = child_node
            else:
                self.parent.left_child = child_node
        elif self.value > self.parent.value:
            self.parent.right_child = child_node
        else:
            self.parent.left_child = child_node


    def _depth(self):
        left_depth = self.left_child._depth() if self.left_child else 0
        right_depth = self.right_child._depth() if self.right_child else 0
        return 1 + max(left_depth, right_depth)

    def balance(self):
        """Check Children and return balance of node."""
        left_weight = self.left_child._depth() if self.left_child else 0
        right_weight = self.right_child._depth() if self.right_child else 0
        return left_weight - right_weight

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

    def _get_dot(self):
        """Recursively prepare a dot graph entry for this node."""
        if self.left_child is not None:
            yield "\t{} -> {};".format(self.value, self.left_child.value)
            for i in self.left_child._get_dot():
                yield i
        elif self.right_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull{} [shape=point];".format(r)
            yield "\t{} -> null{};".format(self.value, r)
        if self.right is not None:
            yield "\t{} -> {};".format(self.value, self.right_child.value)
            for i in self.right_child._get_dot():
                yield i
        elif self.left_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull{} [shape=point];".format(r)
            yield "\t{} -> null{};".format(self.value, r)



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
        """Return Balance of root node.

        If Right is deeper than left, expect a negative integer.
        Expect a positive integer is left size is deeper than right.
        """
        return self.root.balance()

    def _get_right_leftest(self, node):
        while True:
            swap_node = node.right_child.leftest()
            if not swap_node.right_child:
                return swap_node

    def delete(self, value):
        """Delete node with value given, and adjust tree accordingly."""
        node = self._contains(value)
        if not node:
            return False
        self.size -= 1

        if node.right_child and node.left_child:
            swap_node = self._get_right_leftest(node)
            node.value = swap_node.value
            swap_node.orphan_self(None)

        elif node.right_child:
            if node.value == self.root.value:
                self.root = node.right_child
            elif node.value > node.parent.value:
                node.parent.right_child = node.right_child
            else:
                node.parent.left_child = node.right_child

        elif node.left_child:
            if node.value == self.root.value:
                self.root = node.left_child
            elif node.value > node.parent.value:
                node.parent.right_child = node.left_child
            else:
                node.parent.left_child = node.left_child

        if not node.right_child and not node.left_child:
            if node.value == self.root.value:
                self.root = None
                return
            node.orphan_self(None)


    def draw_graph(self):
        if self.root:
            return "digraph G {{\n{}}} \t{};\n{}\n".format(self.root.value, "".join(self.root._get_dot()))


    def delete_for_fun(self, value):
        """Delete node with value given, and adjust tree accordingly.
        MAKE A NEW TREE. O(N^2) FOR THE WIN.
        """
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
