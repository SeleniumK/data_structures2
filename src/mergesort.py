def merge_sort(lst):
    """Sort list using the mergesort method."""

    half = len(lst) // 2
    left_side = lst[:half]
    right_side = lst[half:]

    while left_side and right_side:
        if left_side:
            merge_sort(left_side)
        if right_side:
            merge_sort(right_side)

        i = 0
        while left_side and right_side:
            if left_side[0] > right_side[0]:
                lst[i] = right_side.pop(0)
            else:
                lst[i] = left_side.pop(0)
            i += 1

        for side in (left_side, right_side):
            while side:
                lst[i] = side.pop(0)
                i += 1
