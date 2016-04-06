"""Implement Binary Search Tree."""


class Node(object):
    """Create Node Object."""

    def __init__(self, value=None, left_child=None, right_child=None):
        """Initialize Node Object."""
        self.value = value
        self._left_child = left_child
        self._right_child = right_child

    @property
    def left_child(self):
        """Mask private left_child."""
        return self._left_child

    @left_child.setter
    def left_child(self, value):
        """Set left_child of node if no current left_child."""
        if isinstance(value, Node) and self._left_child is None:
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
        if isinstance(value, Node) and self._right_child is None:
            self._right_child = value
        else:
            raise TypeError
