import pytest
from itertools import permutations
from src.quicksort import quick_sort

TO_SORT = (
    [[]] +
    [[1]]+
    list(map(list, permutations(range(4))))+
    list(map(list, permutations(range(6))))
)


@pytest.mark.parametrize("lst", TO_SORT)
def test_quick(lst):
    copy = lst[:]
    assert quick_sort(lst) == sorted(copy)
