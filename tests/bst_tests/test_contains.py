def test_empty_tree_contains(empty_bst):
    assert not empty_bst.contains(5)


def test_contains(empty_bst):
    """Assert that tree contains nodes."""
    empty_bst.insert(4)
    assert empty_bst.contains(4)


def test_contains_more_nodes(empty_bst):
    """Assert that tree contains nodes."""
    empty_bst.insert(4)
    empty_bst.insert(2)
    empty_bst.insert(3)
    empty_bst.insert(1)
    assert empty_bst.contains(4)
    assert empty_bst.contains(2)
    assert empty_bst.contains(3)
    assert empty_bst.contains(1)


def test_contains_is_false(empty_bst):
    """Assert that tree does not contain nodes."""
    empty_bst.insert(4)
    empty_bst.insert(2)
    empty_bst.insert(3)
    empty_bst.insert(1)
    assert not empty_bst.contains(7)


def test_contains_is_false2(empty_bst):
    """Assert that tree does not contain value."""
    empty_bst.insert(4)
    empty_bst.insert(7)
    empty_bst.insert(6)
    assert not empty_bst.contains(3)
