def test_in_order(bst_root_fifty):
    assert list(bst_root_fifty.in_order()) == [12, 25, 35, 50, 75, 100, 150]


def test_pre_order(bst_root_fifty):
    assert list(bst_root_fifty.pre_order()) == [50, 25, 12, 35, 100, 75, 150]


def test_post_order(bst_root_fifty):
    assert list(bst_root_fifty.post_order()) == [12, 35, 25, 75, 150, 100, 50]


def test_breadth_first(bst_root_fifty):
    assert list(bst_root_fifty.breadth_first()) == [50, 25, 100, 12, 35, 75, 150]


def test_empty_tree_traversals(empty_bst):
    assert list(empty_bst.pre_order()) == []
    assert list(empty_bst.post_order()) == []
    assert list(empty_bst.in_order()) == []
    assert list(empty_bst.breadth_first()) == []
