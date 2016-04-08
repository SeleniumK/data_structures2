import pytest
from bst import Node, Bst
import random


@pytest.fixture
def bst_root_fifty():
    test_tree = Bst()
    test_tree.insert(50)
    test_tree.insert(25)
    test_tree.insert(100)
    test_tree.insert(12)
    test_tree.insert(35)
    test_tree.insert(75)
    test_tree.insert(150)
    return test_tree


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
    test_node.left_child = child_node
    assert test_node.left_child is child_node
    assert child_node.parent is test_node


def test_add_left_child2():
    """Assert successful adding of left child using dot notation."""
    child_node = Node()
    test_node = Node()
    test_node.left_child = child_node
    assert test_node.left_child is child_node


def test_add_left_child_expect_error():
    """Assert that you cannot assign a child to a node when that sided child
    already exists.
    """
    child_node = Node()
    test_node = Node(left_child=child_node)
    with pytest.raises(TypeError):
        test_node.left_child = child_node


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


def test_add_right_child_expect_error():
    """Assert that you cannot assign a child to a node when that sided child
    already exists.
    """
    child_node = Node()
    test_node = Node(right_child=child_node)
    with pytest.raises(TypeError):
        test_node.right_child = child_node


def test_insert_nonnumber():
    """Assert insert with a non numerical value raises type error."""
    test_tree = Bst()
    with pytest.raises(TypeError):
        test_tree.insert("foo")


def test_insert_empty_tree():
    """Assert that insert works on an empty tree."""
    test_tree = Bst()
    test_tree.insert(1)
    assert test_tree.root.value == 1


def test_insert_left_child_tree():
    """Assert that insert left child works as expected."""
    test_tree = Bst()
    test_tree.insert(1)
    test_tree.insert(0)
    assert test_tree.root.left_child.value == 0


def test_insert_right_child_tree():
    """Assert that insert right child works as expected."""
    test_tree = Bst()
    test_tree.insert(1)
    test_tree.insert(0)
    test_tree.insert(4)
    assert test_tree.root.right_child.value == 4
    test_tree.insert(7)
    test_tree.insert(-2)


def test_insert_duplicate():
    """Assert that insert does not work on duplicate values."""
    test_tree = Bst()
    test_tree.insert(1)
    assert test_tree.insert(1) is None
    test_tree.insert(2)
    assert test_tree.insert(2) is None
    assert test_tree.root.right_child.right_child is None
    test_tree.insert(-2)
    assert test_tree.root.left_child.value == -2


def test_contains():
    """Assert that tree contains nodes."""
    test_tree = Bst()
    test_tree.insert(4)
    assert test_tree.contains(4)


def test_contains_more_nodes():
    """Assert that tree contains nodes."""
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(3)
    test_tree.insert(1)
    assert test_tree.contains(4)
    assert test_tree.contains(2)
    assert test_tree.contains(3)
    assert test_tree.contains(1)


def test_contains_is_false():
    """Assert that tree does not contain nodes."""
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(3)
    test_tree.insert(1)
    assert not test_tree.contains(7)

def test_contains_is_false2():
    """Assert that tree does not contain value."""
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(7)
    test_tree.insert(6)
    assert not test_tree.contains(3)


def test_size():
    """Assert that size returns integer representing total number of nodes."""
    test_tree = Bst()
    for x in range(100):
        test_tree.insert(random.randint(0, 100))
        assert test_tree.size() == x + 1

def test_balance_balanced():
    """Assert that if tree is balanced, the balance method returns 0."""
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(5)
    assert test_tree.balance() == 0


def test_balance_unbalanced_to_left():
    """Assert that an unbalanced graph skewed to left returns appropriate
    negative number.
    """
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(5)
    test_tree.insert(1)
    test_tree.insert(0)
    assert test_tree.balance() == -2


def test_balance_unbalanced_to_right():
    """Assert that an unbalanced graph skewed to right returns appropriate
    positive number.
    """
    test_tree = Bst()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(5)
    test_tree.insert(7)
    test_tree.insert(8)
    test_tree.insert(9)
    test_tree.insert(10)
    test_tree.insert(11)
    test_tree.insert(12)
    assert test_tree.balance() == 6


def test_depth():
    """Assert that calling depth returns maximum depth of tree."""
    test_tree = Bst()
    test_tree.insert(4)
    assert test_tree.depth() == 1
    test_tree.insert(2)
    assert test_tree.depth() == 2
    test_tree.insert(5)
    assert test_tree.depth() == 2
    test_tree.insert(7)
    test_tree.insert(8)
    test_tree.insert(9)
    test_tree.insert(10)
    test_tree.insert(11)
    test_tree.insert(12)
    assert test_tree.depth() == 8


def test_bst_fixture(bst_root_fifty):
    assert bst_root_fifty.root.value == 50
    assert bst_root_fifty.depth() == 3


def test_in_order(bst_root_fifty):
    assert list(bst_root_fifty.in_order()) == [12, 25, 35, 50, 75, 100, 150]


def test_pre_order(bst_root_fifty):
    assert list(bst_root_fifty.pre_order()) == [50, 25, 12, 35, 100, 75, 150]


def test_post_order(bst_root_fifty):
    assert list(bst_root_fifty.post_order()) == [12, 35, 25, 75, 150, 100, 50]


def test_breadth_first(bst_root_fifty):
    assert list(bst_root_fifty.breadth_first()) == [50, 25, 100, 12, 35, 75, 150]
