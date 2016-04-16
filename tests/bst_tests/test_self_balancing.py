from itertools import permutations
from src.bst import Bst
import pytest


THREE_NODE_TREE = list(map(list, permutations(range(3))))
FOUR_NODE_TREE = list(map(list, permutations(range(4))))
FIVE_NODE_TREE = list(map(list, permutations(range(5))))
SIX_NODE_TREE = list(map(list, permutations(range(6))))
SEVEN_NODE_TREE = list(map(list, permutations(range(7))))


@pytest.mark.parametrize("tree_list", THREE_NODE_TREE)
def test_balance_3_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    assert list(tree.breadth_first()) == [1, 0, 2]

@pytest.mark.parametrize("tree_list", THREE_NODE_TREE)
def test_balance_3_nodes_delete(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    for i in range(3):
        tree.delete(i)
    assert tree.balance() in [1, 0, -1]

@pytest.mark.parametrize("tree_list", FOUR_NODE_TREE)
def test_balance_4_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    assert tree.balance() in [-1, 0, 1]


@pytest.mark.parametrize("tree_list", FOUR_NODE_TREE)
def test_balance_4_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    assert tree.balance() in [-1, 0, 1]


@pytest.mark.parametrize("tree_list", FIVE_NODE_TREE)
def test_balance_5_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    assert tree.balance() in [-1, 0, 1]


@pytest.mark.parametrize("tree_list", SIX_NODE_TREE)
def test_balance_6_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
        assert tree.balance() in [-1, 0, 1]


def test_balance_4_nodes_delete():
    tree = Bst()
    for i in [3, 1, 0, 2]:
        tree.insert(i)
        assert tree.balance() in [-1, 0, 1]
    tree.delete(0)
    assert tree.balance() in [-1, 0, 1]


def test_delete_root(bst_root_fifty):
    bst_root_fifty.delete(50)
    assert not bst_root_fifty.contains(50)
    assert bst_root_fifty.balance() in [-1, 0, 1]
    assert list(bst_root_fifty.breadth_first()) == [75, 25, 100, 12, 35, 150]


def test_delete_root2(bst_root_fifty):
    bst_root_fifty.delete(25)
    bst_root_fifty.delete(35)
    assert bst_root_fifty.balance() in [-1, 0, 1]
    bst_root_fifty.delete(50)
    assert bst_root_fifty.balance() in [-1, 0, 1]


def test_three():
    tree = Bst()
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(4.5)
    tree.insert(5)
    tree.delete(2)
    assert not tree.contains(2)

def test_balance1():
    tree = Bst()
    lst = [5, 3, 2, 4, 1, 0]
    for i in lst:
        tree.insert(i)
    assert list(tree.breadth_first()) == [3, 1, 5, 0, 2, 4]
    tree.delete(0)
    assert list(tree.breadth_first()) == [3, 1, 5, 2, 4]
    tree.delete(1)
    assert list(tree.breadth_first()) == [3, 2, 5, 4]
    tree.delete(2)
    assert not tree.contains(2)

@pytest.mark.parametrize("tree_list", SIX_NODE_TREE)
def test_balance_4_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
    tree.delete(0)
    tree.delete(1)
    tree.delete(2)
    assert not tree.contains(2)

@pytest.mark.parametrize("tree_list", SIX_NODE_TREE)
def test_balance_6_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
        assert tree.balance() in [-1, 0, 1]
    for i in range(6):
        tree.delete(i)
        assert not tree.contains(i)
        assert tree.balance() in [-1, 0, 1]

@pytest.mark.parametrize("tree_list", SIX_NODE_TREE)
def test_balance_6_nodes_insert(tree_list):
    tree = Bst()
    for i in tree_list:
        tree.insert(i)
        assert tree.balance() in [-1, 0, 1]
    for i in range(6):
        tree.delete(i)
        assert not tree.contains(i)
        assert tree.balance() in [-1, 0, 1]
