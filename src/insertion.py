def insertion_sort(lst):
    # import pdb; pdb.set_trace()
    for i, node in enumerate(lst):
        before = i - 1
        while before >= 0:
            if lst[i] < lst[before]:
                lst[before], lst[i] = lst[i], lst[before]
            before -= 1
    return lst

if __name__ == "__main__":
    pass
