import pytest
from itertools import permutations
from src.mergesort import merge_sort

TO_SORT = (
    [[]] +
    [[1]] +
    list(map(list, permutations(range(4)))) +
    list(map(list, permutations(range(5))))
)


@pytest.mark.parametrize("lst", TO_SORT)
def test_merge1(lst):
    copy = lst[:]
    merge_sort(lst)
    assert lst == sorted(copy), copy
