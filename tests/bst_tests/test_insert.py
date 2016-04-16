import pytest


def test_insert_nonnumber(empty_bst):
    """Assert insert with a non numerical value raises type error."""
    with pytest.raises(TypeError):
        empty_bst.insert("foo")


def test_insert_empty_tree(empty_bst):
    """Assert that insert works on an empty tree."""
    empty_bst.insert(1)
    assert empty_bst.root.value == 1


def test_insert_left_child_tree(empty_bst):
    """Assert that insert left child works as expected."""
    empty_bst.insert(1)
    empty_bst.insert(0)
    assert empty_bst.root.left_child.value == 0


def test_insert_right_child_tree(empty_bst):
    """Assert that insert right child works as expected."""
    empty_bst.insert(1)
    assert empty_bst.root.value == 1
    assert empty_bst.root.left_child is None
    assert empty_bst.root.right_child is None
    assert empty_bst.root.parent is None
    empty_bst.insert(0)
    assert empty_bst.root.left_child.value == 0
    assert empty_bst.root.left_child.parent.value == 1
    assert empty_bst.root.right_child is None
    assert empty_bst.root.right_child is None
    empty_bst.insert(4)
    assert empty_bst.root.right_child.value == 4
    empty_bst.insert(7)
    empty_bst.insert(-2)


def test_insert_duplicate(empty_bst):
    """Assert that insert does not work on duplicate values."""
    empty_bst.insert(1)
    assert empty_bst.insert(1) is None
    empty_bst.insert(2)
    assert empty_bst.insert(2) is None
    assert empty_bst.root.right_child.right_child is None
    empty_bst.insert(-2)
    assert empty_bst.root.left_child.value == -2
