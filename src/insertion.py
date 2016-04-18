from itertools import permutations

def insertion_sort(lst):
    new_lst = lst[:]
    for i, node in enumerate(lst):
        before = i - 1
        current = i
        while before >= 0:
            if new_lst[current] < new_lst[before]:
                new_lst[before], new_lst[current] = new_lst[current], new_lst[before]
            before -= 1
            current -= 1
    return new_lst


if __name__ == "__main__":
    
