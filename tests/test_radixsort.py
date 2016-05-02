import pytest
from itertools import permutations
from src.radix import radix_sort

TO_SORT = (
    [[]] +
    [[1]] +
    list(map(list, permutations(range(2)))) +
    list(map(list, permutations(range(6)))) +
    list(map(list, permutations(range(9, 12))))
)


@pytest.mark.parametrize("lst", TO_SORT)
def test_radix(lst):
    copy = lst[:]
    assert list(radix_sort(lst)) == sorted(copy)


def test_valueerror_radix():
    lst = ["foo", "sarah"]
    with pytest.raises(ValueError):
        radix_sort(lst)
