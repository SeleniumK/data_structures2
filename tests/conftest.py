import pytest
from src.bst import Bst, Node

# BST Fixtures
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


@pytest.fixture
def three_bst():
    test_tree = Bst()
    test_tree.insert(50)
    test_tree.insert(25)
    test_tree.insert(100)
    return test_tree


@pytest.fixture
def empty_bst():
    return Bst()
