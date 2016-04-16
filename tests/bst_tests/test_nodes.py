from src.bst import Node


def test_create_node_default():
    """Assert that you can create a node with no children."""
    test_node = Node()
    assert test_node.value is None
    assert test_node.left_child is None
    assert test_node.right_child is None


def test_add_left_child():
    """Assert successful adding of left child and setting of child's parent."""
    child_node = Node()
    test_node = Node()
    child_node.parent = test_node
    assert test_node.left_child is child_node
    assert child_node.parent is test_node


def test_add_left_child2():
    """Assert successful adding of left child using dot notation."""
    child_node = Node()
    test_node = Node()
    test_node.left_child = child_node
    assert test_node.left_child is child_node


def test_add_right_child():
    """Assert successful adding of right child in instantiation of node."""
    child_node = Node()
    test_node = Node(right_child=child_node)
    assert test_node.right_child is child_node


def test_add_right_child2():
    """Assert successful adding of right child using dot notation."""
    child_node = Node()
    test_node = Node()
    test_node.right_child = child_node
    assert test_node.right_child is child_node
