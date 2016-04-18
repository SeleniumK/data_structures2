import pytest
from itertools import permutations
from src.insertion import insertion_sort


LIST_THREE = list(map(list, permutations(range(3))))


@pytest.mark.parametrize("lst", LIST_THREE)
def test_insertion(lst):
    assert insertion_sort(lst) == [0, 1, 2]
