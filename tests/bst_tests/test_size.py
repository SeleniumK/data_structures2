import random


def test_empty_tree_size(empty_bst):
    assert empty_bst.size() == 0


def test_size(empty_bst):
    """Assert that size returns integer representing total number of nodes."""
    test_tree = empty_bst
    for x in range(100):
        test_tree.insert(random.randint(0, 100))
        assert test_tree.size() == x + 1
