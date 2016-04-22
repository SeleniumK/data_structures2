from itertools import chain


def radix_sort(lst):
    if lst:
        for i in range(1, len(str(max(lst))) + 1):
            buckets = [[] for x in range(10)]
            for item in map(str, lst):
                buckets[int(item[-i]) if i <= len(item) else 0].append(item)
            lst = chain(*buckets)
    return map(int, lst)


if __name__ == "__main__":
    import timeit
    from random import randint
    times = 500

    def test1():
        radix_sort([2, 1])

    def test2():
        radix_sort([randint(0, 1000000) for i in range(1000)])

    avg_time = timeit.Timer(test1).timeit(times)
    avg_time_big = timeit.Timer(test2).timeit(times)

    print("""wat.""")
    print()

    print("Input: [2, 1]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time))
    print()
    print("Input: [randint(0, 1000000) for i in range(1000)]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time_big))
