import pytest
from src.bst import Bst, Node
from src.trie import Trie

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


@pytest.fixture
def simple_trie():
    x = Trie()
    x.insert("Norton")
    x.insert("North")
    x.insert("Nortron")
    x.insert("Nord")
    return x
