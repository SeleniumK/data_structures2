"""Implement Binary Search Tree."""
from collections import deque
import random


class Node(object):
    """Create Node Object. At this point, Node.Value must be a number."""

    def __init__(self, value=None, left_child=None, right_child=None, parent=None):
        """Initialize Node Object."""
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self._parent = parent

    @property
    def parent(self):
        """Return Parent Property."""
        return self._parent

    @parent.setter
    def parent(self, node):
        """Set the parent of the node, and set the appropriate child of parent."""
        self._parent = node
        if node is None:
            self._parent = None
        elif isinstance(node, Node):
            if self.value > node.value:
                node.right_child = self
            else:
                node.left_child = self
        else:
            raise TypeError

    def leftest(self):
        """Get the Leftest Child of this node."""
        return self.left_child.leftest() if self.left_child else self

    def orphan_self(self, child):
        """Connect given child to the parent of this node, on the correct side."""
        if self.value >= self.parent.value:
            self.parent.right_child = child
        else:
            self.parent.left_child = child


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
        if not self.contains(value):
            new_node = Node(value=value)
            self._size += 1
            if self.root is None:
                self.root = new_node
            else:
                cursor = self.root
                while True:
                    if new_node.value > cursor.value:
                        if cursor.right_child is None:
                            new_node.parent = cursor
                            self.check_balance(cursor)
                            return
                        cursor = cursor.right_child
                    else:
                        if cursor.left_child is None:
                            new_node.parent = cursor
                            self.check_balance(cursor)
                            return
                        cursor = cursor.left_child

    def check_balance(self, node):
        """Check node's balance. Rebalances accordingly and updates parent balance."""
        current_balance = node.balance()
        if current_balance > 1 or current_balance < -1:
            self.rebalance(node)
        elif node.parent and node.parent.balance() != 0:
            self.check_balance(node.parent)

    def rotate_left(self, node):
        """Rotate node to the left, make node.right_child new subtree root."""
        swap = node.right_child
        swap.orphan_self(swap.left_child)
        if node == self.root:
            self.root = swap
        swap.parent = node.parent
        node.parent = swap

    def rotate_right(self, node):
        """Rotate node to the right, make node.left_child new subtree root."""
        swap = node.left_child
        swap.orphan_self(swap.right_child)
        if node == self.root:
            self.root = swap
        swap.parent = node.parent
        node.parent = swap

    def rebalance(self, node):
        """Rebalance nodes."""
        if node.balance() < 0:
            if node.right_child.balance() > 0:
                self.rotate_right(node.right_child)
            self.rotate_left(node)
        elif node.balance > 0:
            if node.left_child.balance() < 0:
                self.rotate_left(node.left_child)
            self.rotate_right(node)

    def _contains(self, value):
        """Helper function: returns node matching value."""
        cursor = self.root
        while cursor:
            if cursor.value == value:
                return cursor
            cursor = cursor.right_child if value > cursor.value else cursor.left_child

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

    def _delete_node_with_two_children(self, node):
        swap_node = self._get_right_leftest(node)
        parent = swap_node.parent
        node.value = swap_node.value
        swap_node.orphan_self(None)
        # self.check_balance(parent)

    def _delete_node(self, node, child):  # child can be a node or None
        if node.value == self.root.value:
            self.root = child
        else:
            node.orphan_self(child)
        # self.check_balance(child)

    def delete(self, value):
        """Delete node with value given, and adjust tree accordingly."""
        node = self._contains(value)
        if node:
            self._size -= 1
            if node.right_child and node.left_child:
                self._delete_node_with_two_children(node)
            else: 
                child = node.right_child if node.right_child else node.left_child
                self._delete_node(node, child)

    def draw_graph(self):
        """Draw dot graph."""
        if self.root:
            return "digraph G {{\n{}}} \t{};\n{}\n".format(self.root.value, "".join(self.root._get_dot()))
