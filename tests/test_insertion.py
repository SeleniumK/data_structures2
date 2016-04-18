import pytest
from itertools import permutations
from src.insertion import insertion_sort


THREE = list(map(list, permutations(range(3))))
FOUR = list(map(list, permutations(range(4))))
FIVE = list(map(list, permutations(range(5))))


@pytest.mark.parametrize("lst", THREE)
def test_insertion(lst):
    assert insertion_sort(lst) == [0, 1, 2]


@pytest.mark.parametrize("lst", FOUR)
def test_insertion(lst):
    assert insertion_sort(lst) == [0, 1, 2, 3]


@pytest.mark.parametrize("lst", FIVE)
def test_insertion(lst):
    assert insertion_sort(lst) == [0, 1, 2, 3, 4]
