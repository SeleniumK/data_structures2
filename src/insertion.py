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
    import timeit
    from random import randint
    times = 500

    def test1():
        insertion_sort([2, 1])

    def test2():
        insertion_sort([randint(0, 1000000) for i in range(1000)])

    avg_time = timeit.Timer(test1).timeit(times)
    avg_time_big = timeit.Timer(test2).timeit(times)

    print("""Insertion sort iterates, consuming one input element each repetition,
and growing a sorted output list. Each iteration, insertion sort removes one element
from the input data, finds the location it belongs within the sorted list,
and inserts it there. It repeats until no input elements remain.""")
    print()

    print("Input: [2, 1]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time))
    print()
    print("Input: [randint(0, 1000000) for i in range(1000)]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time_big))
