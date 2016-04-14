import pytest
from src.bst import Node, Bst
import random


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
    assert test_tree.root.value == 1
    assert test_tree.root.left_child is None
    assert test_tree.root.right_child is None
    assert test_tree.root.parent is None
    test_tree.insert(0)
    assert test_tree.root.left_child.value == 0
    assert test_tree.root.left_child.parent.value == 1
    assert test_tree.root.right_child is None
    assert test_tree.root.right_child is None
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

def test_simple_balance_left(empty_bst):
    empty_bst.insert(5)
    empty_bst.insert(3)
    assert empty_bst.balance() == 1

def test_simple_balance_right(empty_bst):
    empty_bst.insert(5)
    empty_bst.insert(7)
    assert empty_bst.balance() == -1

def test_simple_balance_right2(empty_bst):
    empty_bst.insert(5)
    empty_bst.insert(3)
    empty_bst.insert(7)
    empty_bst.insert(8)
    assert empty_bst.balance() == -1

def test_simple_balance_left2(empty_bst):
    empty_bst.insert(5)
    empty_bst.insert(2)
    empty_bst.insert(7)
    empty_bst.insert(1)
    assert empty_bst.balance() == 1

def test_not_so_simple_balance_left(empty_bst):
    empty_bst.insert(90)
    empty_bst.insert(25)
    empty_bst.insert(45)
    empty_bst.insert(12)
    empty_bst.insert(6)
    empty_bst.insert(100)
    empty_bst.insert(150)
    assert empty_bst.balance() == 1

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
    assert test_tree.balance() == 2


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
    assert test_tree.balance() == -6


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


def test_empty_tree_size(empty_bst):
    assert empty_bst.size() == 0


def test_empty_tree_contains(empty_bst):
    assert not empty_bst.contains(5)


def test_empty_tree_depth(empty_bst):
    assert empty_bst.depth() == 0


def test_empty_tree_traversals(empty_bst):
    assert list(empty_bst.pre_order()) == []
    assert list(empty_bst.post_order()) == []
    assert list(empty_bst.in_order()) == []
    assert list(empty_bst.breadth_first()) == []


def test_get_right_leftest(empty_bst):
    empty_bst.insert(50)
    empty_bst.insert(49)
    empty_bst.insert(100)
    node = empty_bst._contains(50)
    assert empty_bst._get_right_leftest(node).value == 100


def test_delete_empty(empty_bst):
    empty_bst.delete(7)
    assert empty_bst.root is None


def test_delete_with_no_children(empty_bst):
    empty_bst.insert(7)
    assert empty_bst.root.value == 7
    empty_bst.delete(7)
    assert empty_bst.root is None

def test_delete_middle_root(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.root.value == 50


def test_remove_still_has_other_node(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.contains(12)


def test_delete_middle_root_llchild(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.root.left_child.left_child.left_child is None


def test_delete_middle_root_left_child(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.root.left_child.value == 35


def test_delete_middle_root_lrchild(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.root.left_child.right_child is None


def test_delete_middle_root_lrchildparent(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert bst_root_fifty.root.left_child.left_child.value == 12


def test_delete_middle_not_contains(bst_root_fifty):
    bst_root_fifty.delete(25)
    assert not bst_root_fifty.contains(25)


def test_delete_root(bst_root_fifty):
    bst_root_fifty.delete(50)
    root = bst_root_fifty.root
    assert root.value == 75
    assert root.right_child.value == 100
    assert root.left_child.value == 25
    assert root.right_child.right_child.value == 150
    assert root.right_child.left_child is None
    assert root.left_child.right_child.value == 35
    assert root.left_child.left_child.value == 12


def test_delete_node_both_children(bst_root_fifty):
    bst_root_fifty.delete(100)
    assert not bst_root_fifty.contains(100)
    assert bst_root_fifty.root.right_child.left_child.value == 75
    assert bst_root_fifty.root.right_child.value == 150
    assert bst_root_fifty.root.right_child.right_child is None


def test_delete_node_both_children_root(bst_root_fifty):
    bst_root_fifty.delete(50)
    assert bst_root_fifty.root.value == 75


def test_delete_parent(bst_root_fifty):
    bst_root_fifty.insert(30)
    bst_root_fifty.insert(37)
    bst_root_fifty.delete(35)
    root_grandchild = bst_root_fifty.root.left_child.right_child
    assert root_grandchild.value == 37
    assert root_grandchild.left_child.value == 30
    assert root_grandchild.right_child is None


def test_delete_grampa(bst_root_fifty):
    bst_root_fifty.insert(6)
    bst_root_fifty.insert(13)
    bst_root_fifty.delete(25)
    root_left_child = bst_root_fifty.root.left_child
    assert root_left_child.value == 35
    assert root_left_child.left_child.value == 12
    assert root_left_child.right_child is None


def test_delete_parent_one_child(bst_root_fifty):
    bst_root_fifty.insert(6)
    bst_root_fifty.delete(12)
    root_left_child = bst_root_fifty.root.left_child
    assert root_left_child.value == 25
    assert root_left_child.left_child.value == 6
    assert root_left_child.left_child.left_child is None


def test_delete_parent_one_child_right(bst_root_fifty):
    bst_root_fifty.insert(27)
    bst_root_fifty.delete(35)
    root_left_child = bst_root_fifty.root.left_child
    assert root_left_child.value == 25
    assert root_left_child.right_child.value == 27


def test_delete_parent_two_children(bst_root_fifty):
    bst_root_fifty.insert(6)
    bst_root_fifty.insert(13)
    bst_root_fifty.delete(12)
    root_left_child = bst_root_fifty.root.left_child
    assert root_left_child.value == 25
    assert root_left_child.left_child.value == 13
    assert root_left_child.left_child.left_child.value == 6


def test_two_node_bst(empty_bst):
    empty_bst.insert(100)
    empty_bst.insert(75)
    empty_bst.insert(150)
    empty_bst.delete(100)
    assert empty_bst.root.value == 150






















