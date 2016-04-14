def test_balance_balanced(empty_bst):
    """Assert that if tree is balanced, the balance method returns 0."""
    empty_bst.insert(4)
    empty_bst.insert(2)
    empty_bst.insert(5)
    assert empty_bst.balance() == 0


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


def test_balance_unbalanced_to_left(empty_bst):
    """Assert that an unbalanced graph skewed to left returns appropriate negative number."""
    empty_bst.insert(4)
    empty_bst.insert(2)
    empty_bst.insert(5)
    empty_bst.insert(1)
    empty_bst.insert(0)
    assert empty_bst.balance() == 2


def test_balance_unbalanced_to_right(empty_bst):
    """Assert that an unbalanced graph skewed to right returns appropriate positive number."""
    empty_bst.insert(4)
    empty_bst.insert(2)
    empty_bst.insert(5)
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(12)
    assert empty_bst.balance() == -6
