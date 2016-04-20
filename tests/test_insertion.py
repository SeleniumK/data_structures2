import pytest
from itertools import permutations
from src.insertion import insertion_sort

TO_SORT = (
    [[]] +
    [[1]] +
    list(map(list, permutations(range(3)))) +
    list(map(list, permutations(range(4)))) +
    list(map(list, permutations(range(5))))
)


@pytest.mark.parametrize("lst", TO_SORT)
def test_insertion(lst):
    assert insertion_sort(lst) == sorted(lst)
