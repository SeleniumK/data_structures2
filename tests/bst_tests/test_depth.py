def test_empty_tree_depth(empty_bst):
    assert empty_bst.depth() == 0


def test_depth(empty_bst):
    """Assert that calling depth returns maximum depth of tree."""
    empty_bst.insert(4)
    assert empty_bst.depth() == 1
    empty_bst.insert(2)
    assert empty_bst.depth() == 2
    empty_bst.insert(5)
    assert empty_bst.depth() == 2
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(12)
    # before self balancing functionality
    # assert empty_bst.depth() == 8
    # after self balancing functionality
    assert empty_bst.depth() == 4


def test_bst_fixture_depth(bst_root_fifty):
    assert bst_root_fifty.root.value == 50
    assert bst_root_fifty.depth() == 3
