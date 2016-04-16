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
    assert root_left_child.value ==12 
    assert root_left_child.left_child.value == 6
    assert root_left_child.right_child.value == 35


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
